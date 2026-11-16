---
name: cv-tailor
description: Udržuje komplexní hlavní CV a profesní profil Martina Hájka a připravuje z nich specializované životopisy, motivační dopisy a medailonky pro konkrétní firmy. Použij pro jeho profesní podklady, výběr doložených zkušeností a odevzdání zkompilované verze v tomto repozitáři.
---

# CV Tailor — Martin Hájek

Před obsahovou prací přečti celý [profesní profil](references/professional-profile.md). Obsahuje úplný inventář znalostí, pracovní a akademické zkušenosti, zdroje tvrzení i otevřené otázky. Kontakty načítej z kořenového `info.tex`, včetně GitHubu. Nová přímá potvrzení uživatele mají přednost před historickými CV.

## Hlavní CV a specializované verze

`main` obsahuje komplexní hlavní CV: profesní profil, zaměstnání a konkrétní činnosti, vzdělání, všechny potvrzené technologické oblasti, AI zaměření, jasně označené základní znalosti a jazyky. Je to obsahový základ pro další přihlášky. Udržuj jej ucelený, věcný a profesionální; délku řeš čitelnou sazbou a uspořádáním, ne vynecháním podstatných zkušeností nebo drobným písmem.

Pro konkrétní firmu vyber a seřaď relevantní zkušenosti z hlavního CV a profilu. Uprav úvod, důraz pracovních bodů, výběr technologií a případný motivační dopis podle nabídky. Zachovej doložená fakta a požadovaný jazyk. Specializovaná verze může být kratší; úzké zaměření jedné přihlášky nepřenášej zpět do `main`.

## Oblasti, které má profil pokrývat

- **Vývoj:** full-stack podnikové aplikace v C#/.NET, TypeScriptu, Reactu a Angularu; interní systémy kvality a výrobní logistiky, REST API a databáze. Další potvrzené backendové a frontendové technologie vybírej z inventáře v profilu.
- **Integrace a provoz:** MES, SAP, SharePoint, autentizace, GitLab a GitLab CI/CD, IIS, Docker a Linux. Odděluj doloženou pracovní činnost od obecné znalosti nástroje.
- **Mezinárodní projekty:** spolupráce s vývojovými týmy a německými závody, pracovní komunikace v angličtině, v některých případech vedení projektu.
- **Koordinace dodavatele v KAMAX:** komunikace s externím partnerem, kontrola postupu a řešení otevřených bodů v týdenních sprintech. Konkrétní kontext je zavádění MES na platformě Ignition; podle nabídky lze zdůraznit platformu, nebo obecnější koordinaci dodávky softwaru.
- **AI:** zájem o AI, LLM API a prompt engineering, propojování LLM s aplikacemi a nástroji, MCP servery a obecné principy návrhu AI agentů. AI agents/MCP/smolagents je společně hodnocená položka. LangChain a LangGraph uživatel nově uvedl mezi AI znalostmi 2026-11-16, bez samostatného hodnocení hloubky nebo pracovního použití. Akademický kontext tvoří neuronové sítě v bakalářské práci a predikce výroby FVE v diplomové práci.
- **Vzdělání a jazyky:** Aplikovaná informatika na TUL, Ing. s vyznamenáním; čeština rodilá, angličtina B1/B2 s pracovní komunikací. Úroveň němčiny ani oficiální jazyková certifikace potvrzené nejsou.

## Úroveň a přesnost tvrzení

- YES potvrzuje znalost nebo používání, nikoli automaticky profesionální praxi, senioritu, počet let nebo dokončený projekt.
- Java je doložená pouze ve školních projektech; Python ve školních projektech a AI kurzech podle přímého upřesnění 2026-11-16. Neuváděj u nich pracovní praxi ani dobu používání bez dalšího potvrzení. Uživatel nemá konkrétní samostatný AI/LLM projekt k popsání v CV; AI prezentuj pomocí potvrzených frameworků, MCP a konceptů, ne vymyšleným projektem.
- BASICS vždy označ jako základní znalost. NO neuváděj jako dovednost. Zachovej společně hodnocené skupiny; neodvozuj zvláštní úroveň každé dílčí technologie.
- Aktuální zaměstnání KAMAX uživatel potvrdil 2026-11-16 a odkázal na chronologii profilu: 06/2022–08/2024 a 01/2025–dosud, ioLabs 09/2024–11/2024. Období KAMAX neslučuj do nepřetržitého zaměstnání.
- Koordinace sprintů není důkazem formální role Scrum Master, Product Owner či Project Manager. Koordinace zavádění Ignition nedokládá jeho programování, administraci ani architektonickou odpovědnost.
- Znalosti AI a akademické práce nedokládají komerční AI projekt nebo produkční nasazení. AWS, Azure a společná položka Azure AI/AWS Bedrock zůstávají BASICS.
- Nepřidávej výsledkové metriky, certifikace, absolvovaná školení ani rozsah odpovědnosti bez podkladu. Pokud je cílový výstup potřebuje, upřesni konkrétní chybějící údaj s uživatelem a pokračuj v podložených částech.

## Větev a zadání

Novou přihlášku zakládej z aktuální lokální `main`; zachovej rozpracované změny. Použij `python3 scripts/cv.py new --company "Firma" --position "Pozice" --brief-file /tmp/zadani.txt`, případně úlohu **CV: Nová přihláška** ve VS Code. V souboru musí být celé původní zadání.

Větev pojmenuj podle firmy, malými písmeny bez diakritiky, s pomlčkami místo mezer. Další přihlášky do stejné firmy čísluj `firma-2`, `firma-3` atd., i při stejné pozici. Úpravy již existující přihlášky zůstávají v její větvi. Pozici nepřidávej do názvu větve.

README dané větve musí obsahovat firmu, pozici, celé původní zadání, pozdější upřesnění a odkaz na výstup. `application.json` musí odpovídat skutečné větvi a jazyku verze.

## Sazba, kompilace a odevzdání

Používej profesionální sazbu s dobře čitelným písmem a výraznější barevnou hierarchií. Aktuální návrh má tmavě modrou hlavičku, tyrkysové akcenty a světlé modré podklady znalostí. Uživatel požádal o živější vzhled místo převážně šedé sazby. Technologie, AI a základní znalosti spoj do jedné sekce „Technické znalosti“. Rozvrhni ji do textových řádků: vlevo název oblasti, vpravo seznam technologií. AI je jednou z oblastí vedle backendu, frontendu, databází či cloudu. Základní úroveň označ přímo u konkrétní technologie nebo společně hodnocené skupiny; nevytvářej samostatnou sekci základních znalostí. Technologické ikony a svislé oddělovače uživatel odmítl jako nepřehledné. Text musí jít z PDF kopírovat. Nepřidávej neověřená procenta znalostí ani hodnoticí pruhy.

Do výchozího profesního CV nezařazuj fitness, posilovnu ani obecné sportovní zájmy. Uživatel je 2026-11-16 označil za zbytečné pro tento výstup; historický údaj může zůstat v podkladech. Zájmy přidávej, pokud je uživatel znovu požaduje nebo mají konkrétní vztah k přihlášce.

Uživatelem dodaný portrét je v `assets/images/picture.png`. Hlavní CV používá větší obdélník na výšku vpravo v barevné hlavičce, s bílým rámečkem. Uživatel preferuje menší přiblížení s prostorem kolem hlavy a ramen a ořez zejména po stranách. Ořez je řešený viewportem v LaTeXu; nepřepisuje zdrojový obrázek ani nedeformuje proporce. Při odvozování verzí zachovej cestu, společné zarovnání a dostatek místa pro text hlavičky.

Osobní GitHub v kontaktech vede na profil uživatele. Odkaz v patičce vede na **repozitář v aktuální větvi**, například `https://github.com/HajekMartin/CV/tree/firma-2`. Nesmí vést přímo na PDF. Generuje jej build skript z Git větve a `origin`.

Po úpravě CV spusť `python3 scripts/cv.py build` nebo výchozí build úlohu ve VS Code. Prohlédni všechny stránky PDF v `output/`, ověř text, diakritiku, přetečení a oba GitHub odkazy. PDF patří do stejné verze jako zdroje a README; `.build/` je dočasná. Odevzdej odkaz na hotové PDF a stručně popiš změny a ověření.

## Údržba podkladů

Nové výslovné údaje uživatele zapisuj do profilu s datem a původem. Odděluj hodnocení znalosti od konkrétního použití. Odvozené nové CV není nezávislým důkazem pro tvrzení v profilu; uchovávej původ historických podkladů. Nové údaje o projektu nepřepočítávají původních 50 technologických odpovědí, pokud uživatel výslovně nemění hodnocení.
