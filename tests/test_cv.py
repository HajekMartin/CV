import argparse
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch


SOURCE_ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("cv", SOURCE_ROOT / "scripts" / "cv.py")
cv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cv)


class NamingTests(unittest.TestCase):
    def test_company_names_and_monotonic_numbering(self):
        self.assertEqual(cv.slug("Škoda Auto, a.s."), "skoda-auto-a-s")
        self.assertEqual(cv.next_branch("Škoda Auto", set()), "skoda-auto")
        self.assertEqual(cv.next_branch("Škoda Auto", {"skoda-auto"}), "skoda-auto-2")
        self.assertEqual(cv.next_branch("Škoda Auto", {"skoda-auto-2", "skoda-auto-12"}), "skoda-auto-13")

    def test_github_remote_formats(self):
        for remote in (
            "https://github.com/HajekMartin/CV.git",
            "git@github.com:HajekMartin/CV.git",
            "ssh://git@github.com/HajekMartin/CV.git",
        ):
            self.assertEqual(cv.repository_url(remote), "https://github.com/HajekMartin/CV")


class ApplicationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="cv-workflow-")
        self.addCleanup(self.temporary.cleanup)
        parent = Path(self.temporary.name)
        self.root = parent / "work"
        self.root.mkdir()
        self.remote = parent / "origin.git"
        subprocess.run(["git", "init", "--bare", str(self.remote)], check=True, capture_output=True)
        self.root_patch = patch.object(cv, "ROOT", self.root)
        self.root_patch.start()
        self.addCleanup(self.root_patch.stop)
        cv.git("init", "-b", "main")
        cv.git("config", "user.name", "Workflow Test")
        cv.git("config", "user.email", "test@example.invalid")
        cv.git("remote", "add", "origin", str(self.remote))
        (self.root / "templates").mkdir()
        shutil.copyfile(SOURCE_ROOT / "templates" / "application-readme.md", self.root / "templates" / "application-readme.md")
        shutil.copyfile(SOURCE_ROOT / ".gitignore", self.root / ".gitignore")
        shutil.copyfile(SOURCE_ROOT / "application.json", self.root / "application.json")
        (self.root / "body.tex").write_text("Shared template\n")
        (self.root / "README.md").write_text("Template README\n")
        (self.root / "output").mkdir()
        (self.root / "output" / "CV-Martin-Hajek-main.pdf").write_bytes(b"%PDF-template")
        self.commit("Initial template")
        cv.git("push", "-u", "origin", "main")
        self.brief = parent / "brief.txt"
        self.brief.write_text("Celé původní zadání.\nReact, C# a AI; text s $ a `kódem`.\n", encoding="utf-8")
        self.args = argparse.Namespace(company="Škoda Auto", position="Software Engineer", brief_file=str(self.brief), language="cs")

    def commit(self, message):
        cv.git("add", ".")
        cv.git("commit", "-m", message)

    def test_application_preserves_brief_and_starts_from_main(self):
        cv.new_application(self.args)
        self.assertEqual(cv.git("branch", "--show-current"), "skoda-auto")
        readme = (self.root / "README.md").read_text()
        self.assertIn(self.brief.read_text().strip(), readme)
        self.assertIn("output/CV-Martin-Hajek-skoda-auto.pdf", readme)
        self.assertEqual(json.loads((self.root / "application.json").read_text())["branch"], "skoda-auto")
        self.assertFalse((self.root / "output" / "CV-Martin-Hajek-main.pdf").exists())
        (self.root / "body.tex").write_text("First application only\n")
        self.commit("First application")
        cv.new_application(self.args)
        self.assertEqual(cv.git("branch", "--show-current"), "skoda-auto-2")
        self.assertEqual((self.root / "body.tex").read_text(), "Shared template\n")
        self.assertEqual(cv.git("show", "main:README.md"), "Template README")

    def test_remote_branches_reserve_numbers(self):
        cv.git("push", "origin", "main:skoda-auto-3")
        cv.new_application(self.args)
        self.assertEqual(cv.git("branch", "--show-current"), "skoda-auto-4")

    def test_uncommitted_work_prevents_branch_switch(self):
        (self.root / "body.tex").write_text("Unsaved work\n")
        with self.assertRaisesRegex(ValueError, "není čistý"):
            cv.new_application(self.args)
        self.assertEqual(cv.git("branch", "--show-current"), "main")
        self.assertEqual((self.root / "body.tex").read_text(), "Unsaved work\n")

    def test_footer_links_to_repository_branch(self):
        cv.git("remote", "set-url", "origin", "git@github.com:HajekMartin/CV.git")
        output, url = cv.pdf_location("skoda-auto-2")
        self.assertEqual(output.name, "CV-Martin-Hajek-skoda-auto-2.pdf")
        self.assertEqual(url, "https://github.com/HajekMartin/CV/tree/skoda-auto-2")

    def test_build_rejects_stale_branch_metadata(self):
        cv.git("switch", "-c", "another-company")
        with self.assertRaisesRegex(ValueError, "neodpovídá"):
            cv.build(argparse.Namespace(engine="auto"))

    def test_failed_compilation_does_not_replace_previous_pdf(self):
        cv.git("remote", "set-url", "origin", "https://github.com/HajekMartin/CV.git")
        with patch.object(cv, "find_engine", return_value=("tectonic", shutil.which("false"))), patch.object(cv, "open_document") as opener:
            with self.assertRaisesRegex(ValueError, "Kompilace selhala"):
                cv.build(argparse.Namespace(engine="auto", open_pdf=True))
        opener.assert_not_called()
        self.assertEqual((self.root / "output" / "CV-Martin-Hajek-main.pdf").read_bytes(), b"%PDF-template")

    def test_preview_does_not_open_another_branch_pdf(self):
        cv.git("remote", "set-url", "origin", "https://github.com/HajekMartin/CV.git")
        cv.git("switch", "-c", "skoda-auto")
        with self.assertRaisesRegex(ValueError, "zatím neexistuje"):
            cv.open_pdf(argparse.Namespace())


if __name__ == "__main__":
    unittest.main()
