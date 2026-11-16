# CV — $company — $position

| Údaj | Hodnota |
| --- | --- |
| Firma | $company |
| Pozice | $position |
| Větev | `$branch` |
| Jazyk CV | `$language` |

Výstup: [CV-Martin-Hajek-$branch.pdf](output/CV-Martin-Hajek-$branch.pdf).

Tato větev obsahuje jednu konkrétní přihlášku odvozenou z komplexního hlavního CV na `main`. Její zdroje, zadání a PDF se udržují společně. Odkaz v patičce PDF vede na repozitář v této větvi: [github.com/HajekMartin/CV/tree/$branch](https://github.com/HajekMartin/CV/tree/$branch). Bude dostupný po nahrání větve na GitHub. Osobní GitHub v kontaktech zůstává odkazem na profil.

## Původní zadání

$brief

## Úpravy a sestavení

Obsah `body.tex` přizpůsobit zadání podle [profesního profilu](skills/cv-tailor/references/professional-profile.md) a [skillu cv-tailor](skills/cv-tailor/SKILL.md). Konkrétní provedené úpravy a případná upřesnění zadání doplnit do tohoto README, původní zadání zachovat.

```sh
python3 scripts/cv.py build
```

Ve Visual Studio Code nejprve ulož soubory a stiskni **Cmd+Shift+B** (macOS) nebo **Ctrl+Shift+B** (Windows/Linux). Úloha **CV: Sestavit a otevřít PDF** zkompiluje tuto větev a otevře výsledné PDF. Přes **Terminal → Run Task…** lze také jen sestavit nebo otevřít poslední PDF.

Kompilace potřebuje Tectonic, XeLaTeX nebo LuaLaTeX. Pomocné soubory jsou v `.build/`; hotové PDF v `output/` se ukládá do této větve. Před dokončením ověřit sazbu, diakritiku, cílovou firmu a odkaz v patičce.
