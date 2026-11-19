---
name: cv-tailor
description: Udržuje komplexní hlavní CV, profesní profil a projektové podklady pro případné portfolio Martina Hájka a připravuje z nich specializované životopisy, průvodní a motivační dopisy (cover letter) a medailonky pro konkrétní firmy. Použij pro jeho profesní podklady, výběr doložených zkušeností a odevzdání výstupů v tomto repozitáři.
---

# CV Tailor — Martin Hájek

Před obsahovou prací přečti celý [profesní profil](references/professional-profile.md). Obsahuje úplný inventář znalostí, pracovní a akademické zkušenosti, zdroje tvrzení i otevřené otázky. Kontakty načítej z kořenového `info.tex`, včetně GitHubu. Nová přímá potvrzení uživatele mají přednost před historickými CV.

## Hlavní CV a specializované verze

`main` obsahuje komplexní hlavní CV: profesní profil, zaměstnání a konkrétní činnosti, vzdělání, všechny potvrzené technologické oblasti, AI zaměření, jasně označené základní znalosti a jazyky. Výchozí PDF neobsahuje samostatné portfolio projektů. Je to obsahový základ pro další přihlášky. Udržuj jej ucelený, věcný a profesionální; délku řeš čitelnou sazbou a uspořádáním, ne vynecháním podstatných zkušeností nebo drobným písmem.

Pro konkrétní firmu vyber a seřaď relevantní zkušenosti z hlavního CV a profilu. Uprav úvod, důraz pracovních bodů, výběr technologií a případný motivační dopis podle nabídky. Zachovej doložená fakta a požadovaný jazyk. Specializovaná verze může být kratší; úzké zaměření jedné přihlášky nepřenášej zpět do `main`.

Projektové podklady jsou uložené pro nabídky, které požadují portfolio. V takovém případě vyber relevantní příklady do odpovědi nebo samostatného přehledu: účel, osobní role, doložený kontext a u veřejných kurzových ukázek odkaz na repozitář. Rozlišuj pracovní projekty KAMAX a učební příklady Hugging Face/Laba. Volitelnou sazbu poskytuje `portfolio.tex`, který výchozí `body.tex` nenačítá. Portfolio připoj přímo do CV pouze na výslovné zadání uživatele. Zdroj faktů a omezení rolí zůstává v profesním profilu. Tuto preferenci uživatel výslovně upřesnil 2026-11-19.

## Oblasti, které má profil pokrývat

- **Vývoj:** full-stack podnikové aplikace v C#/.NET, TypeScriptu, Reactu a Angularu; interní systémy kvality a výrobní logistiky, REST API a databáze. Další potvrzené backendové a frontendové technologie vybírej z inventáře v profilu.
- **Integrace a provoz:** MES, SAP, SharePoint, autentizace, GitLab a GitLab CI/CD, IIS, Docker a Linux. Odděluj doloženou pracovní činnost od obecné znalosti nástroje.
- **Pracovní portfolio:** Smart Shopfloor hostovaný v AWS — přizpůsobení a zavedení v KAMAX Turnov, MES integrace; obměna MES — člen projektového týmu; mezinárodní .NET aplikace — spolupráce s IT týmy v Německu na vývoji a integraci pro závody TUR. Přesné role a hranice tvrzení jsou v profesním profilu.
- **Mezinárodní projekty:** spolupráce s IT týmy v Německu na vývoji .NET řešení a integraci pro závody TUR, pracovní komunikace v angličtině, u vybraných projektů vedení.
- **Koordinace dodavatele v KAMAX:** komunikace s externím partnerem, kontrola postupu a řešení otevřených bodů v týdenních sprintech. Konkrétní kontext je zavádění MES na platformě Ignition; podle nabídky lze zdůraznit platformu, nebo obecnější koordinaci dodávky softwaru.
- **AI:** zájem o AI, LLM API a prompt engineering, propojování LLM s aplikacemi a nástroji, MCP servery a obecné principy návrhu AI agentů. AI agents/MCP/smolagents je společně hodnocená položka. LangChain a LangGraph uživatel nově uvedl mezi AI znalostmi 2026-11-16, bez samostatného hodnocení hloubky nebo pracovního použití. Akademický kontext tvoří neuronové sítě v bakalářské práci a predikce výroby FVE v diplomové práci.
- **Vzdělání a jazyky:** Aplikovaná informatika na TUL, Ing. s vyznamenáním; čeština rodilá, angličtina B2 s pracovní komunikací. Uživatel B2 výslovně potvrdil 2026-11-16 jako vlastní hodnocení. Úroveň němčiny ani oficiální jazyková certifikace potvrzené nejsou.

## Úroveň a přesnost tvrzení

- YES potvrzuje znalost nebo používání, nikoli automaticky profesionální praxi, senioritu, počet let nebo dokončený projekt.
- Java je doložená pouze ve školních projektech; Python ve školních projektech a AI kurzech podle přímého upřesnění 2026-11-16. Neuváděj u nich pracovní praxi ani dobu používání bez dalšího potvrzení. Od 2026-11-19 jsou doložené kurzové repozitáře Hugging Face a Laba; použij konkrétní příklady z profilu v kurzovém kontextu. Komerční AI projekt zatím potvrzený není.
- BASICS vždy označ jako základní znalost. NO neuváděj jako dovednost. Zachovej společně hodnocené skupiny; neodvozuj zvláštní úroveň každé dílčí technologie.
- Aktuální zaměstnání KAMAX uživatel potvrdil 2026-11-16 a odkázal na chronologii profilu: 06/2022–08/2024 a 01/2025–dosud, ioLabs 09/2024–11/2024. Období KAMAX neslučuj do nepřetržitého zaměstnání.
- Koordinace sprintů není důkazem formální role Scrum Master, Product Owner či Project Manager. Koordinace zavádění Ignition nedokládá jeho programování, administraci ani architektonickou odpovědnost.
- Znalosti AI a akademické práce nedokládají komerční AI projekt nebo produkční nasazení. AWS, Azure a společná položka Azure AI/AWS Bedrock zůstávají BASICS.
- U Smart Shopfloor je AWS doložený jako prostředí aplikace. Potvrzená role se týká přizpůsobení, zavedení používání a MES integrací; nevyvozuj z ní správu cloudové infrastruktury ani vyšší obecnou úroveň AWS.
- Nepřidávej výsledkové metriky, certifikace, absolvovaná školení ani rozsah odpovědnosti bez podkladu. Pokud je cílový výstup potřebuje, upřesni konkrétní chybějící údaj s uživatelem a pokračuj v podložených částech.

## Cover letter na požádání

Dopis vytvářej na výslovné požádání, samostatně nebo spolu s CV. Před psaním zjisti dvě volby: **délku** a **styl**. Pokud některá chybí, zeptej se na ni; obě chybějící volby nabídni současně a před vytvořením dopisu vyčkej na odpověď. Volbu uvedenou už v aktuálním zadání znovu nepotvrzuj. Zadání „úplně krátký, věcný cover letter“ tedy další otázku nepotřebuje. Tyto volby platí pro daný dopis, nikoli automaticky pro další přihlášky.

| Délka | Rozsah |
| --- | --- |
| Úplně krátká | Nejvýše 5 vět těla dopisu; stručné a přirozeně dlouhé věty. Oslovení, podpis a závěrečný LinkedIn se do limitu nepočítají. |
| Střední | Přibližně 150–220 slov těla dopisu ve 3–4 krátkých odstavcích. |

Jiný výslovně zadaný limit má přednost.

| Styl | Důraz |
| --- | --- |
| Motivační | Proč mě zajímá daná role a její zaměření, kam se chci profesně posunout a čím mohu přispět. Motivaci opři o uživatelem uvedené zájmy a doložené zaměření pozice. |
| Věcný | Konkrétní požadavky nabídky spoj s relevantními, doloženými zkušenostmi a jejich přínosem pro práci. |
| Kombinovaný | Krátká konkrétní motivace a několik nejrelevantnějších zkušeností. Nabídni jako doporučenou vyváženou variantu. |

Firmu, pozici a kontext načti z aktuální přihlášky; jazyk přebírej z `application.json`, pokud uživatel nepožádá o jiný. Pro každou délku i styl platí stejná pravidla důkazů jako pro CV. Nezaměňuj zájem o oblast nebo znalost frameworku za pracovní zkušenost. U motivačního stylu nevymýšlej osobní příběh, dlouhodobý vztah k firmě ani její kulturu. Věcný styl může být plynulý text; nemusí mít podobu seznamu.

Na úplný konec **každého** dopisu, za podpis, vždy přidej samostatný řádek `LinkedIn: https://www.linkedin.com/in/<mylinkedin>/`. Hodnotu `mylinkedin` načti z `info.tex`; aktuálně odpovídá profilu `hajek-martin`. V souboru zachovej úplnou URL, v chatu může být klikací. Za tento řádek už nepatří další obsah dopisu.

Hotový text předlož v chatu ke snadnému zkopírování a ulož ve větvi dané přihlášky jako `output/Cover-Letter-Martin-Hajek-<větev>.txt`. PDF připrav, pokud jej uživatel požaduje. Dopis ani volby a odpovědi z chatu nekopíruj do README. Před odevzdáním ověř rozsah, styl, doloženost tvrzení, jazyk a závěrečný LinkedIn. Tato pravidla uživatel doplnil 2026-11-16.

## Větev a popis pozice

Novou přihlášku zakládej z aktuální lokální `main`; zachovej rozpracované změny. Použij `python3 scripts/cv.py new --company "Firma" --position "Pozice" --job-url "https://example.com/pozice"`, případně úlohu **CV: Nová přihláška** ve VS Code. Odkaz na inzerát je volitelný. Osobní zadání z chatu slouží k práci s CV a nekopíruje se do README.

Větev pojmenuj podle firmy, malými písmeny bez diakritiky, s pomlčkami místo mezer. Další přihlášky do stejné firmy čísluj `firma-2`, `firma-3` atd., i při stejné pozici. Úpravy již existující přihlášky zůstávají v její větvi. Pozici nepřidávej do názvu větve.

README dané větve obsahuje veřejný popis pozice, odkaz na nabídku a základní údaje: firmu, pozici, jazyk CV, větev a odkaz na PDF. Neuváděj osobní prompt, citace z chatu, doplňující odpovědi ani interní poznámky o kandidátovi nebo tvorbě CV. `application.json` musí odpovídat skutečné větvi a jazyku verze.

## Sazba, kompilace a odevzdání

Používej profesionální sazbu s dobře čitelným písmem a výraznější barevnou hierarchií. Aktuální návrh má tmavě modrou hlavičku, tyrkysové akcenty a světlé modré podklady znalostí. Uživatel požádal o živější vzhled místo převážně šedé sazby. Technologie, AI a základní znalosti spoj do jedné sekce „Technické znalosti“. Rozvrhni ji do textových řádků: vlevo název oblasti, vpravo seznam technologií. AI je jednou z oblastí vedle backendu, frontendu, databází či cloudu. Základní úroveň označ přímo u konkrétní technologie nebo společně hodnocené skupiny; nevytvářej samostatnou sekci základních znalostí. Technologické ikony a svislé oddělovače uživatel odmítl jako nepřehledné. Text musí jít z PDF kopírovat. Nepřidávej neověřená procenta znalostí ani hodnoticí pruhy.

Do výchozího profesního CV nezařazuj fitness, posilovnu ani obecné sportovní zájmy. Uživatel je 2026-11-16 označil za zbytečné pro tento výstup; historický údaj může zůstat v podkladech. Zájmy přidávej, pokud je uživatel znovu požaduje nebo mají konkrétní vztah k přihlášce.

Uživatelem dodaný portrét je v `assets/images/picture.png`. Hlavní CV používá větší obdélník na výšku vpravo v barevné hlavičce, s bílým rámečkem. Uživatel preferuje menší přiblížení s prostorem kolem hlavy a ramen a ořez zejména po stranách. Ořez je řešený viewportem v LaTeXu; nepřepisuje zdrojový obrázek ani nedeformuje proporce. Při odvozování verzí zachovej cestu, společné zarovnání a dostatek místa pro text hlavičky.

Osobní GitHub v kontaktech vede na profil uživatele. Odkaz v patičce vede na **repozitář v aktuální větvi**, například `https://github.com/HajekMartin/CV/tree/firma-2`. Nesmí vést přímo na PDF. Generuje jej build skript z Git větve a `origin`.

Po úpravě CV spusť `python3 scripts/cv.py build` nebo výchozí build úlohu ve VS Code. Prohlédni všechny stránky PDF v `output/`, ověř text, diakritiku, přetečení a oba GitHub odkazy. PDF patří do stejné verze jako zdroje a README; `.build/` je dočasná. Odevzdej odkaz na hotové PDF a stručně popiš změny a ověření.

## Údržba podkladů

Nové výslovné údaje uživatele zapisuj do profilu s datem a původem. Odděluj hodnocení znalosti od konkrétního použití. Odvozené nové CV není nezávislým důkazem pro tvrzení v profilu; uchovávej původ historických podkladů. Nové údaje o projektu nepřepočítávají původních 50 technologických odpovědí, pokud uživatel výslovně nemění hodnocení.
