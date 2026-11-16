# Pokyny pro práci s CV Martina Hájka

Tento repozitář obsahuje LaTeXový životopis a podklady pro jeho přizpůsobení pracovním nabídkám.

## Šablona a jednotlivé přihlášky

- `main` udržuj jako komplexní hlavní CV a společnou šablonu: úplný profesní profil, zkušenosti, vzdělání a potvrzené oblasti znalostí. Každé nové zadání přihlášky zpracuj ve vlastní větvi vytvořené z aktuální `main`, ve které CV podle potřeby zkrátíš a zaměříš na nabídku.
- Název větve odvozuj výhradně od firmy, malými písmeny, bez diakritiky, s pomlčkami místo mezer. Opakované přihlášky čísluj `firma-2`, `firma-3` atd., i při stejné pozici. Úprava již existující přihlášky zůstává v její větvi.
- Pro založení přihlášky používej `python3 scripts/cv.py new --company "Firma" --position "Pozice" --brief-file /tmp/zadani.txt`. Skript kontroluje místní i aktualizované vzdálené větve a vychází z lokální `main`; předem zajisti, že obsahuje aktuální šablonu. Rozpracované změny uživatele zachovej.
- Celé uživatelovo zadání a případně text inzerátu ulož do README dané větve. Zachovej původní znění a doplň firmu, pozici i pozdější upřesnění. `application.json` musí odpovídat této přihlášce.
- Po každé úpravě obsahu nebo sazby spusť `python3 scripts/cv.py build`, zkontroluj PDF a odevzdej odkaz na hotový soubor v `output/`. PDF patří do verze spolu se zdroji a README; dočasné soubory z `.build/` nikoli.
- Patička PDF musí odkazovat na repozitář v aktuální větvi na GitHubu, například `https://github.com/HajekMartin/CV/tree/firma-2`, nikoli přímo na PDF. Odkaz generuje build skript z aktuální větve a `origin`; zkontroluj jej i ve výsledném PDF. Osobní GitHub v kontaktech vede na profil z `info.tex`.

## Profil a lokální skill

- Před psaním nebo obsahovou úpravou CV, motivačního dopisu či profesního medailonku přečti [skill cv-tailor](skills/cv-tailor/SKILL.md).
- Zdrojem profesních údajů je [profesní profil](skills/cv-tailor/references/professional-profile.md). Obsahuje zkušenosti, úrovně znalostí, zaměření na AI a dosud nevyjasněné údaje.
- Nová výslovná potvrzení uživatele mají přednost před staršími podklady. Při aktualizaci profilu uveď datum a původ doplnění; rozlišuj potvrzené informace a otevřené otázky.
- Potvrzená znalost technologie sama o sobě nedokládá její použití v zaměstnání, délku praxe ani expertní úroveň. Úroveň BASICS zachovej jako základní znalost; položky NO neuváděj mezi dovednostmi.
- Zájem o AI, znalost MCP serverů, propojování LLM a obecná znalost tvorby AI agentů jsou výslovně potvrzené. Uživatel 2026-11-16 doplnil mezi AI znalosti LangChain a LangGraph; jejich přesnou úroveň a pracovní použití zatím neupřesnil. Konkrétní pracovní AI projekty a jejich výsledky zatím doložené nejsou.
- Uváděj mezinárodní projekty a koordinaci externího dodavatele v KAMAX, včetně pravidelných týdenních sprintů. Konkrétní kontext je zavádění MES na platformě Ignition; nejde o samostatné potvrzení implementační znalosti platformy ani formální Scrum role.

## Soubory životopisu

- `main.tex` obsahuje sazbu a načítá `info.tex` a `body.tex`. Sestavuje se přes `scripts/cv.py build`, který doplní větev, odkaz a jazyk z `application.json`.
- `info.tex` je zdroj jména a kontaktů. Cesta `assets/info.tex` ze starších podkladů v tomto repozitáři neexistuje.
- `assets/images/picture.png` je uživatelem dodaný portrét. Vpravo v tmavě modré hlavičce se zobrazuje větší obdélník na výšku v bílém rámečku, s menším přiblížením a prostorem kolem hlavy a ramen. Zužuje se hlavně po stranách. Ořez je nastavený v LaTeXu; zdrojový obrázek zůstává zachovaný. Používej stejný soubor i v odvozených verzích.
- `body.tex` na `main` je komplexní hlavní CV; obsahové podklady a úrovně znalostí jsou v profesním profilu. Nepovažuj nově odvozený text CV za nezávislý zdroj nových tvrzení.
- Uživatel 2026-11-16 potvrdil aktuální zaměstnání KAMAX a odkázal na podrobnou chronologii v profilu: KAMAX 06/2022–08/2024 a 01/2025–dosud, ioLabs 09/2024–11/2024. Období KAMAX neslučuj do nepřetržitého zaměstnání.
- Design udržuj profesionální a barevně výraznější: tmavě modrá hlavička, tyrkysové akcenty a světlé modré podklady znalostí. Technologie, AI a základní znalosti spoj do jednoho přehledu „Technické znalosti“ s textovými řádky podle oblastí, bez technologických ikon a svislých oddělovačů. Základní úroveň označ přímo u příslušných technologií; nezakládej pro ni samostatnou sekci. Fitness a obecné sportovní zájmy do výchozího profesního CV nezařazuj. Kontroluj všechny stránky PDF.
- Při změnách LaTeXu zachovej existující strukturu a správně escapuj speciální znaky.
