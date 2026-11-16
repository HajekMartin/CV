#!/usr/bin/env python3
"""Create company branches and build the matching, linked CV PDF."""

import argparse
import json
import os
from pathlib import Path
import re
import shutil
from string import Template
import subprocess
import sys
import unicodedata
from urllib.parse import quote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = {"cs": "czech", "en": "english", "de": "ngerman"}


def git(*args):
    return subprocess.run(
        ["git", *args], cwd=ROOT, check=True, capture_output=True, text=True
    ).stdout.strip()


def slug(text):
    ascii_text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    result = re.sub(r"[^a-z0-9]+", "-", ascii_text.lower()).strip("-")
    if not result:
        raise ValueError("Název musí obsahovat alespoň jedno písmeno nebo číslici.")
    return result


def next_branch(company, existing):
    base = slug(company)
    numbers = [1] if base in existing else []
    for branch in existing:
        match = re.fullmatch(re.escape(base) + r"-([2-9]|[1-9][0-9]+)", branch)
        if match:
            numbers.append(int(match.group(1)))
    return f"{base}-{max(numbers) + 1}" if numbers else base


def repository_url(remote):
    if remote.startswith("git@github.com:"):
        remote = "https://github.com/" + remote.split(":", 1)[1]
    elif remote.startswith("ssh://git@github.com/"):
        remote = "https://github.com/" + remote.split("github.com/", 1)[1]
    parts = urlsplit(remote)
    path = parts.path.rstrip("/").removesuffix(".git")
    if parts.hostname != "github.com" or len(path.strip("/").split("/")) != 2:
        raise ValueError("Remote origin musí odkazovat na GitHub repozitář.")
    return "https://github.com" + path


def pdf_location(branch):
    filename = f"CV-Martin-Hajek-{slug(branch)}.pdf"
    repo = repository_url(git("remote", "get-url", "origin"))
    url = f"{repo}/tree/{quote(branch, safe='')}"
    return ROOT / "output" / filename, url


def new_application(args):
    brief = Path(args.brief_file).expanduser().read_text(encoding="utf-8")
    if not brief.strip() or not args.company.strip() or not args.position.strip():
        raise ValueError("Firma, pozice i zadání musí být vyplněné.")
    if any(char in args.company + args.position for char in "\r\n"):
        raise ValueError("Firma a pozice musí být na jednom řádku.")
    if git("status", "--porcelain"):
        raise ValueError("Pracovní strom není čistý. Nejprve ulož rozpracované změny.")
    git("rev-parse", "--verify", "refs/heads/main")
    git("fetch", "--prune", "origin")
    refs = git("for-each-ref", "--format=%(refname)", "refs/heads", "refs/remotes/origin")
    existing = {
        ref.removeprefix("refs/heads/").removeprefix("refs/remotes/origin/")
        for ref in refs.splitlines()
    }
    branch = next_branch(args.company, existing)
    git("check-ref-format", "--branch", branch)
    # Read the template from main even when invoked from an application branch.
    template = Template(git("show", "main:templates/application-readme.md"))
    readme = template.substitute(
        company=args.company, position=args.position, branch=branch,
        language=args.language, brief=brief.rstrip("\n"),
    )
    metadata = {
        "company": args.company, "position": args.position,
        "branch": branch, "language": args.language,
    }
    git("switch", "-c", branch, "main")
    (ROOT / "README.md").write_text(readme + "\n", encoding="utf-8")
    (ROOT / "application.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (ROOT / "output" / "CV-Martin-Hajek-main.pdf").unlink(missing_ok=True)
    print(f"Vytvořena větev {branch}; zadání je v README.md.")
    print("Přizpůsob body.tex a spusť: python3 scripts/cv.py build")


def tex_escape(value):
    escapes = {
        "\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$",
        "#": r"\#", "_": r"\_", "{": r"\{", "}": r"\}",
        "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
    }
    return "".join(escapes.get(char, char) for char in value)


def find_engine(requested):
    names = [requested] if requested != "auto" else ["tectonic", "xelatex", "lualatex"]
    for name in names:
        local = ROOT / ".tools" / name
        executable = str(local) if os.access(local, os.X_OK) else shutil.which(name)
        if executable:
            return name, executable
    raise ValueError("Chybí LaTeX kompilátor. Nainstaluj Tectonic, XeLaTeX nebo LuaLaTeX; viz README.")


def build(args):
    branch = git("branch", "--show-current")
    if not branch:
        raise ValueError("Kompilace potřebuje pojmenovanou Git větev, nikoli detached HEAD.")
    metadata = json.loads((ROOT / "application.json").read_text(encoding="utf-8"))
    if metadata.get("branch") != branch:
        raise ValueError("Větev v application.json neodpovídá aktuální Git větvi.")
    if branch != "main" and not (metadata.get("company") and metadata.get("position")):
        raise ValueError("Přihláška musí mít v application.json vyplněnou firmu a pozici.")
    language = metadata.get("language")
    if language not in LANGUAGES:
        raise ValueError("Podporované jazyky v application.json jsou cs, en a de.")
    engine_name, executable = find_engine(args.engine)
    destination, url = pdf_location(branch)
    build_dir = ROOT / ".build" / slug(branch)
    build_dir.mkdir(parents=True, exist_ok=True)
    wrapper = build_dir / "cv.tex"
    label = repository_url(git("remote", "get-url", "origin")).removeprefix("https://")
    wrapper.write_text(
        f"\\newcommand{{\\cvlanguage}}{{{LANGUAGES[language]}}}\n"
        f"\\newcommand{{\\cvversionurl}}{{\\detokenize{{{url}}}}}\n"
        f"\\newcommand{{\\cvversionlabel}}{{{tex_escape(label + ' / ' + branch)}}}\n"
        "\\input{main.tex}\n",
        encoding="utf-8",
    )
    intermediate = build_dir / "cv.pdf"
    intermediate.unlink(missing_ok=True)
    env = os.environ.copy()
    env["TECTONIC_CACHE_DIR"] = str(ROOT / ".cache" / "tectonic")
    # Classic engines use TEXINPUTS; Tectonic needs its own search-path option.
    env["TEXINPUTS"] = str(ROOT) + os.pathsep + env.get("TEXINPUTS", "")
    if engine_name == "tectonic":
        command = [executable, "-Z", f"search-path={ROOT}", "--keep-logs", "--keep-intermediates", "--outdir", str(build_dir), str(wrapper)]
        passes = 1  # Tectonic handles reruns itself.
    else:
        command = [executable, "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", "-no-shell-escape", f"-output-directory={build_dir}", str(wrapper)]
        passes = 2
    log_path = build_dir / "build.log"
    with log_path.open("w", encoding="utf-8") as log:
        for _ in range(passes):
            result = subprocess.run(command, cwd=ROOT, env=env, stdout=log, stderr=subprocess.STDOUT)
            if result.returncode:
                break
    if result.returncode:
        tail = "\n".join(log_path.read_text(errors="replace").splitlines()[-30:])
        raise ValueError(f"Kompilace selhala; log: {log_path}\n{tail}")
    if not intermediate.is_file() or not intermediate.read_bytes().startswith(b"%PDF-"):
        raise ValueError("Kompilátor nevytvořil platný výstup PDF.")
    tex_log = (build_dir / "cv.log").read_text(errors="replace")
    if "Missing character:" in tex_log:
        raise ValueError(f"Ve výstupu chybí znaky. Zkontroluj {build_dir / 'cv.log'}.")
    destination.parent.mkdir(exist_ok=True)
    temporary = destination.with_suffix(".pdf.tmp")
    shutil.copyfile(intermediate, temporary)
    temporary.replace(destination)
    print(f"PDF: {destination.relative_to(ROOT)}")
    print(f"Odkaz v patičce: {url}")
    if "Overfull \\" in tex_log:
        print(f"Sazba hlásí přesah obsahu; zkontroluj PDF a {build_dir / 'cv.log'}.")
    if getattr(args, "open_pdf", False):
        open_document(destination)


def open_document(path):
    if not path.is_file():
        raise ValueError("PDF pro aktuální větev zatím neexistuje. Nejdříve CV sestav.")
    if sys.platform == "win32":
        os.startfile(str(path))
    else:
        command = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.run([command, str(path)], check=True)
    print(f"Otevřeno PDF: {path.relative_to(ROOT)}")


def open_pdf(args):
    branch = git("branch", "--show-current")
    if not branch:
        raise ValueError("Otevření PDF potřebuje pojmenovanou Git větev, nikoli detached HEAD.")
    destination, _ = pdf_location(branch)
    open_document(destination)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    new = commands.add_parser("new", help="Založit novou přihlášku z main")
    new.add_argument("--company", required=True)
    new.add_argument("--position", required=True)
    new.add_argument("--brief-file", required=True)
    new.add_argument("--language", choices=LANGUAGES, default="cs")
    new.set_defaults(action=new_application)
    compile_cv = commands.add_parser("build", help="Zkompilovat PDF aktuální větve")
    compile_cv.add_argument("--engine", choices=["auto", "tectonic", "xelatex", "lualatex"], default="auto")
    compile_cv.add_argument("--open", dest="open_pdf", action="store_true", help="Po úspěšné kompilaci otevřít PDF")
    compile_cv.set_defaults(action=build)
    preview = commands.add_parser("open", help="Otevřít poslední PDF aktuální větve")
    preview.set_defaults(action=open_pdf)
    args = parser.parse_args()
    try:
        args.action(args)
    except subprocess.CalledProcessError as error:
        detail = (error.stderr or "").strip()
        print(f"Příkaz {error.cmd[0]} selhal (kód {error.returncode}). {detail}", file=sys.stderr)
        return 1
    except (ValueError, OSError, KeyError) as error:
        print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
