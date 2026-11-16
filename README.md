# CV — Martin Hájek

Větev `main` obsahuje komplexní hlavní CV a společnou LaTeXovou šablonu. Zahrnuje pracovní zkušenosti, mezinárodní projekty a koordinaci dodavatele, vzdělání, potvrzené technologie a AI zaměření. Každá nová přihláška vzniká jako specializovaná verze v samostatné větvi podle firmy, se zadáním v jejím `README.md` a výsledným PDF ve složce `output/`.

CV používá dvoustránkovou sazbu s tmavě modrou hlavičkou, tyrkysovými akcenty a světlými modrými podklady znalostí. Větší portrét vpravo má obdélníkový formát na výšku, menší přiblížení a prostor kolem hlavy a ramen. Ořez po stranách je součástí LaTeXu, původní obrázek zůstává zachovaný. Technologie, AI a základní znalosti tvoří jeden přehled „Technické znalosti“, uspořádaný do textových řádků podle oblastí, bez technologických ikon a svislých oddělovačů. Základní úroveň je označená přímo u příslušných technologií. AI zahrnuje LLM API, prompt engineering, MCP, LangChain, LangGraph a koncepty AI agentů. Obecné sportovní zájmy se do výchozího CV nezařazují. Kontakty zahrnují osobní GitHub; samostatný odkaz v patičce vede na repozitář v příslušné větvi.

Názvy větví jsou malými písmeny, bez diakritiky a s pomlčkami místo mezer: například `skoda-auto`. Další přihlášky do stejné firmy dostávají `skoda-auto-2`, `skoda-auto-3` atd., i když jde o stejnou pozici. Úpravy jedné existující přihlášky zůstávají v její větvi. Název pozice se ukládá do README a metadat, nikoli do názvu větve.

## Ovládání z Visual Studio Code

Otevři ve VS Code celou složku tohoto repozitáře přes **File → Open Folder…**. Úlohy jsou připravené v [.vscode/tasks.json](.vscode/tasks.json) a potřebují stejný Python a LaTeX kompilátor jako sestavení z terminálu. Další rozšíření nejsou potřeba.

Ulož upravené soubory a stiskni **Cmd+Shift+B** na macOS nebo **Ctrl+Shift+B** na Windows/Linuxu. Výchozí úloha **CV: Sestavit a otevřít PDF** zkompiluje aktuální větev, uloží PDF do `output/` a po úspěchu je otevře ve výchozím systémovém prohlížeči PDF. Výsledek a případné chyby uvidíš v panelu Terminal. [Výchozí build úloha ve VS Code](https://code.visualstudio.com/docs/debugtest/tasks).

Přes **Terminal → Run Task…** jsou dostupné tyto volby:

| Úloha | Co provede |
| --- | --- |
| **CV: Sestavit a otevřít PDF** | Kompilace a otevření právě vytvořeného PDF |
| **CV: Pouze sestavit PDF** | Kompilace do `output/` |
| **CV: Otevřít poslední PDF** | Otevření uloženého PDF aktuální větve bez kompilace |
| **CV: Nová přihláška** | Formulář pro firmu, pozici, cestu k zadání a jazyk; poté založení větve a README |

Pro novou přihlášku vytvoř v Exploreru složku `.local` a soubor `.local/zadani.txt`, vlož celé zadání a soubor ulož. Tato složka je vynechaná z Gitu, takže příprava zadání neblokuje přepnutí větve. Ostatní rozpracované změny nejprve ulož do commitu přes panel **Source Control**; šablona musí být uložená na `main`. Pak spusť **CV: Nová přihláška** a vyplň vstupy. Přihláška se založí z `main`; po přizpůsobení `body.tex` ji sestavíš stejnou klávesovou zkratkou.

Z terminálu lze stejné otevření spustit pomocí `python3 scripts/cv.py build --open`, případně `python3 scripts/cv.py open` pro již uložené PDF.

## Postup při novém zadání

1. Vycházet z aktuální větve `main`. Rozpracovanou práci nejprve uložit, aby bylo možné bezpečně přepnout větev.
2. Uložit celé uživatelovo zadání nebo text nabídky do dočasného textového souboru a založit přihlášku:

   ```sh
   python3 scripts/cv.py new --company "Škoda Auto" --position "Software Engineer" --brief-file /tmp/zadani.txt
   ```

   Skript aktualizuje přehled vzdálených větví z `origin`, vybere volné pořadové číslo a vytvoří větev z lokální `main`. Zapíše firmu, pozici, větev a celé zadání do README; metadata uloží do `application.json`. Pro jiný jazyk lze přidat `--language en` nebo `--language de`.
3. Přizpůsobit hlavní CV v `body.tex` zadání podle [profesního profilu](skills/cv-tailor/references/professional-profile.md) a [skillu cv-tailor](skills/cv-tailor/SKILL.md). Vybrat a seřadit relevantní zkušenosti, případně zkrátit technologický přehled; úplný základ zůstává na `main`.
4. Zkompilovat CV:

   ```sh
   python3 scripts/cv.py build
   ```

5. Zkontrolovat PDF, text, diakritiku a odkaz v patičce. Výstup pojmenovaný `output/CV-Martin-Hajek-<vetev>.pdf` patří do stejné větve jako zdroje a README.

Skript pro novou přihlášku potřebuje čistý pracovní strom a uloženou šablonu na `main`. Při práci v jiné přihlášce se její obsah nepřenáší do nové větve. Při aktualizaci existující přihlášky stačí upravit její soubory a znovu spustit `build`.

## Kompilace a výstupy

Je potřeba Python 3.10+ a [Tectonic](https://tectonic-typesetting.github.io/book/latest/installation/), případně XeLaTeX nebo LuaLaTeX s potřebnými balíčky TeX Live. Skript hledá Tectonic také v `.tools/tectonic`. Konkrétní kompilátor lze vybrat přes `--engine tectonic`, `--engine xelatex` nebo `--engine lualatex`.

Tectonic při prvním sestavení stahuje potřebné LaTeXové balíčky; jeho cache se ukládá do `.cache/tectonic/`. Pomocné soubory a logy jsou v `.build/`. Tyto složky ani lokální nástroje v `.tools/` se neverzují; hotová PDF v `output/` se verzují.

Kompilaci spouštět přes skript: z aktuální Git větve a adresy `origin` vytvoří kontext pro LaTeX a odkaz na repozitář v této větvi na GitHubu. `application.json` musí odpovídat skutečné větvi. V patičce každé stránky je klikací odkaz na `https://github.com/HajekMartin/CV/tree/<vetev>`, například `tree/main` nebo `tree/skoda-auto-2`. Odkaz nevede přímo na PDF; příslušná větev musí být nahraná na GitHub. Osobní GitHub v kontaktech vede na `https://github.com/HajekMartin`.

Komplexní hlavní CV: [CV-Martin-Hajek-main.pdf](output/CV-Martin-Hajek-main.pdf).

## Soubory

| Soubor | Účel |
| --- | --- |
| `main.tex` | Společná sazba, hlavička a patička s odkazem na danou verzi CV |
| `info.tex` | Jméno a kontaktní údaje včetně GitHubu |
| `assets/images/picture.png` | Zdroj portrétu; do barevné hlavičky se vkládá obdélníkový výřez na výšku |
| `body.tex` | Na `main` komplexní CV; ve firemní větvi obsah přizpůsobený přihlášce |
| `application.json` | Firma, pozice, větev a jazyk této verze |
| `README.md` | Na `main` popis šablony; v přihlášce její údaje a celé zadání |
| `templates/application-readme.md` | Předloha README pro nové přihlášky |
| `scripts/cv.py` | Zakládání přihlášek a kompilace PDF |
| `.vscode/tasks.json` | Úlohy pro sestavení, otevření PDF a novou přihlášku přímo z VS Code |
| `output/` | Hotová PDF určená k uložení spolu s danou verzí |

Kontrola skriptů: `python3 -m unittest discover -s tests -v`.
