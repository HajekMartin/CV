# CV — Air Bank — AI vývojář/ka – interní nástroje

| Údaj | Hodnota |
| --- | --- |
| Firma | Air Bank |
| Pozice | AI vývojář/ka – interní nástroje |
| Větev | `air-bank` |
| Jazyk CV | `cs` |

Výstup: [CV-Martin-Hajek-air-bank.pdf](output/CV-Martin-Hajek-air-bank.pdf).

Tato větev obsahuje jednu konkrétní přihlášku odvozenou z komplexního hlavního CV na `main`. Její zdroje, zadání a PDF se udržují společně. Odkaz v patičce PDF vede na repozitář v této větvi: [github.com/HajekMartin/CV/tree/air-bank](https://github.com/HajekMartin/CV/tree/air-bank). Bude dostupný po nahrání větve na GitHub. Osobní GitHub v kontaktech zůstává odkazem na profil.

## Původní zadání

Připrav mi tedy na tento inzerát nový CV [https://kariera.airbank.cz/pracujte-u-nas/nabidka/ai-engineer-internich-nastroju](https://kariera.airbank.cz/pracujte-u-nas/nabidka/ai-engineer-internich-nastroju)

## Úpravy a sestavení

- Úvod a hlavička jsou zaměřené na interní nástroje, LLM a integrace pro Air Bank.
- Pracovní zkušenosti zdůrazňují analýzu požadavků interních týmů, vývoj podnikových aplikací, integrace, Docker, CI/CD, autentizaci a týmovou spolupráci.
- AI je uvedené na začátku technického přehledu: potvrzené frameworky, MCP a koncepty agentů, bez vymyšleného projektu.
- Python a Java jsou označené svým skutečným kontextem; Azure zůstává základní znalostí. Méně relevantní technologie z hlavního CV byly vynechány.
- Zachovaná je barevná sazba a portrét z `assets/images/picture.png`. Patička vede na repozitář ve větvi `air-bank`.

```sh
python3 scripts/cv.py build
```

Ve Visual Studio Code nejprve ulož soubory a stiskni **Cmd+Shift+B** (macOS) nebo **Ctrl+Shift+B** (Windows/Linux). Úloha **CV: Sestavit a otevřít PDF** zkompiluje tuto větev a otevře výsledné PDF. Přes **Terminal → Run Task…** lze také jen sestavit nebo otevřít poslední PDF.

Kompilace potřebuje Tectonic, XeLaTeX nebo LuaLaTeX. Pomocné soubory jsou v `.build/`; hotové PDF v `output/` se ukládá do této větve. Před dokončením ověřit sazbu, diakritiku, cílovou firmu a odkaz v patičce.

## Nabídka — stručné shrnutí

Zdroj: [AI vývojář/ka — Air Bank](https://kariera.airbank.cz/pracujte-u-nas/nabidka/ai-engineer-internich-nastroju), přečteno 16. 11. 2026. Titulek stránky je „AI vývojář/ka“, původní název v adrese je „AI Engineer interních nástrojů“.

Malý AI tým vyvíjí interní služby a aplikace nad LLM. Náplň zahrnuje agenty, MCP a práci s dokumenty či komunikací; důležité jsou kvalita řešení, předání a spolupráce se zadavateli. Požadovaná je alespoň dvouletá zkušenost s Javou nebo Pythonem. Integrační prostředí využívá Azure, kontejnery a CI/CD; nabídka jmenuje také FastAPI, Go, Kubernetes/Podman, OracleDB, Gerrit a Jenkins. Pozice je v Praze, hybridně, na plný úvazek.

## Upřesnění uživatele a hranice tvrzení

Uživatel při přípravě tohoto CV upřesnil:

> V Javě jen ve školních projektech. V pythonu školní projekty + AI projekty v rámci AI kurzů. Do skillů klidně dopln treba smolagents a spis vyjmenuj jen frameworky co jsou ve skills pro AI a MCP znalost atd. A koncepty. Konkretne nic nemam

Java tedy není vydávána za pracovní praxi, Python je uveden v kontextu školních projektů a AI kurzů. Dva roky praxe v těchto jazycích nejsou potvrzené. Samostatný realizovaný AI/LLM projekt se nevymýšlí; stejně tak nejsou doplněny nepodložené znalosti RAG implementací, FastAPI, Kubernetes, Podman, OracleDB, Gerrit nebo Jenkins. Upřesnění je uložené i do společného profesního profilu na `main` pro další přihlášky.

## Ověření výstupu

- Sestaveno příkazem `python3 scripts/cv.py build`: dvě stránky A4.
- Obě stránky byly vizuálně zkontrolované; kompilace nehlásí přetékání ani chybějící znaky.
- Ověřený je český text, metadata Air Bank, osobní GitHub v kontaktech a odkaz na `https://github.com/HajekMartin/CV/tree/air-bank` v patičce obou stránek.
