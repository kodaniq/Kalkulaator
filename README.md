# 🧮 Kalkulaator

[![CodeQL](https://github.com/kodaniq/Kalkulaator/actions/workflows/codeql.yml/badge.svg)](https://github.com/kodaniq/Kalkulaator/actions/workflows/codeql.yml)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Pythonis kirjutatud käsurea kalkulaator, mis toetab mitme tehtega avaldisi, sulge, teaduslikke funktsioone, matemaatilisi konstante ja arvutuste ajalugu.

## ✨ Funktsioonid

- Mitu tehet ühes avaldises
- Õige tehete järjekord
- Sulud
- Eesti komakohad, näiteks `2,5 + 1,5`
- Implitsiitne korrutamine, näiteks `2pi`, `2(3 + 4)` ja `3sqrt(9)`
- Liitmine, lahutamine, korrutamine (`*`, `x` või `×`), jagamine (`/` või `÷`), astendamine, kalkulaatori-stiilis protsendid ja jääk
- `sqrt`, `abs`, `sin`, `cos`, `tan` ja `log`
- Matemaatilised konstandid `pi` ja `e`
- `ans` eelmise vastuse kasutamiseks
- `undo` viimase arvutuse eemaldamiseks ja eelmise `ans` väärtuse taastamiseks
- `help`, teemakohane `help <teema>`, `history`, ekraani puhastav `clear` ja ajaloo jaoks `clear history`
- Vigaste sisendite kontroll ja täpsemad veateated, näiteks puuduva sulu või vigase tehtemärgi kohta
- Kirjavigade puhul soovitused tuntud funktsioonidele, nimedele ja käskudele
- Turvaline AST-põhine parser ilma `eval()`-ita
- Parseri ja arvutusloogika unit-testid
- Väliseid teeke pole vaja

## 📋 Nõuded

- Python 3.10 või uuem

## ▶️ Käivitamine

```bash
python kalkulaator.py
```

Mõnes süsteemis:

```bash
python3 kalkulaator.py
```

## 💻 Kasutamine

```text
Kalkulaator
Sisesta avaldis, näiteks: (5 + 3) * 2 või sin(30) + cos(60)
Käsud: help, history, undo, clear, clear history

> 5 + 3 * 2
Vastus: 11

> 2,5 + 1,5
Vastus: 4

> 3,14 * 2
Vastus: 6.28

> 5 × 3
Vastus: 15

> 2x(5+26) - 32
Vastus: 30

> 10 ÷ 2
Vastus: 5

> (5 + 3) * 2
Vastus: 16

> 2 ^ 3 + 4
Vastus: 12

> ans / 2 + 7
Vastus: 13

> sin(30) + cos(60)
Vastus: 1

> 2pi
Vastus: 6.283185307

> 2(3 + 4)
Vastus: 14

> 3sqrt(9)
Vastus: 9

> 200 + 15%
Vastus: 230

> 200 - 15%
Vastus: 170

> 200 * 15%
Vastus: 30
```

Tühikud pole kohustuslikud: nii `5+3` kui ka `5 + 3` töötavad. Komakohaga arvudes saab kasutada nii Eesti koma kui ka punkti, näiteks `2,5` või `2.5`. Levinud korrutamistes võib `*` ka ära jätta: `2pi`, `2(3 + 4)`, `3sqrt(9)` ja `(2 + 3)(4 + 5)`.

## ➗ Tehted ja funktsioonid

| Süntaks | Tähendus | Näide |
| --- | --- | --- |
| `+` | Liitmine | `5 + 3` → 8 |
| `-` | Lahutamine | `5 - 3` → 2 |
| `*`, `x` või `×` | Korrutamine | `2x(5+26) - 32` → 30 |
| `/` või `÷` | Jagamine | `6 ÷ 3` → 2 |
| `^` või `**` | Astendamine | `2 ^ 3` → 8 |
| `+ 15%` / `- 15%` | Protsendi lisamine või lahutamine eelnevast arvust | `200 + 15%` → 230 |
| `15%` | Protsent korrutamisel | `200 * 15%` → 30 |
| `%` | Jäägi leidmine kahe arvu vahel | `10 % 3` → 1 |
| `sqrt(x)` | Ruutjuur | `sqrt(9)` → 3 |
| `abs(x)` | Absoluutväärtus | `abs(-5)` → 5 |
| `sin(x)` | Siinus kraadides | `sin(90)` → 1 |
| `cos(x)` | Koosinus kraadides | `cos(180)` → -1 |
| `tan(x)` | Tangens kraadides | `tan(45)` → 1 |
| `log(x)` | Kümnendlogaritm | `log(100)` → 2 |

Korrutamiseks saab kasutada `*`, `x` või `×` ning jagamiseks `/` või `÷`. Näiteks `2x(5+26) - 32` annab 30. Lihtsad funktsioonid töötavad ka ilma sulgudeta, näiteks `sqrt 144`. Implitsiitne korrutamine võimaldab kirjutada loomulikumalt `2pi`, `2(3 + 4)`, `3sqrt(9)` ja `(2 + 3)(4 + 5)` ilma `*` märgita. Astendamiseks saab kasutada nii `^` kui ka `**`. Protsendi saab kirjutada otse arvu järele. Liitmisel ja lahutamisel käitub see nagu tavakalkulaatoris: `200 + 15%` → 230 ja `200 - 15%` → 170. Korrutamisel jääb `200 * 15%` → 30. Tühikutega kahe arvu vahel olev `%` töötab endiselt jäägitehtena.

## 🔢 Konstandid

| Konstant | Tähendus | Näide |
| --- | --- | --- |
| `pi` | π | `2 * pi` → 6.283185307 |
| `e` | Euleri arv | `e ** 2` → 7.389056099 |

Konstante saab kasutada avaldistes samamoodi nagu tavalisi arve. Trigonomeetrilised funktsioonid `sin`, `cos` ja `tan` kasutavad endiselt kraade.

## ⌨️ Käsud

| Käsk | Tegevus |
| --- | --- |
| `help` | Näitab üldist kasutusabi |
| `help <teema>` | Näitab konkreetse funktsiooni või teema abi, nt `help sqrt` |
| `history` | Näitab selle käivituse jooksul tehtud arvutusi |
| `undo` | Eemaldab viimase arvutuse ja taastab eelmise `ans` väärtuse |
| `clear` | Puhastab terminali ekraani |
| `clear history` | Tühjendab arvutuste ajaloo |
| `ans` | Kasutab avaldises eelmist vastust |

## 🆘 Teemakohane abi

Käsuga `help <teema>` saab vaadata ainult vajaliku funktsiooni või võimaluse juhiseid:

```text
> help sqrt

--- Abi: sqrt ---
sqrt(x) — leiab ruutjuure.
Näide: sqrt(144) → 12

> help %

--- Abi: % ---
15% — protsent; kahe arvu vahel olev % on jäägitehe.
Näited: 200 + 15% → 230, 200 - 15% → 170, 200 * 15% → 30, 10 % 3 → 1

> help ans

--- Abi: ans ---
ans — eelmise arvutuse tulemus.
Näide: ans / 2
```

Ka abiteemade ja käskude kirjavigade puhul kasutatakse soovitusi. Näiteks `help sqr` pakub `sqrt`, `histroy` pakub `history` ja `udno` pakub `undo`.

## 🕘 Arvutuste ajalugu

`history` näitab selle käivituse jooksul tehtud avaldisi ja vastuseid nummerdatud loendina. `undo` eemaldab viimase arvutuse ning taastab `ans` väärtuseks eelmise arvutuse tulemuse. Kui ühtegi varasemat arvutust ei jää, muutub `ans` tühjaks. Ajalugu saab tühjendada käsuga `clear history`. Käsk `clear` puhastab ainult terminali ekraani ega kustuta ajalugu.

```text
--- Arvutuste ajalugu ---
1. 5 + 3 * 2 = 11
2. sqrt(144) = 12
3. 2 * pi = 6.283185307

> undo
Eelmine arvutus eemaldatud.
ans = 12
```

## 🔐 Avaldiste turvalisus

Kalkulaator ei kasuta sisendi arvutamiseks `eval()`-i. Avaldis parsitakse Pythoni AST abil ning lubatud on ainult numbrid, kalkulaatori matemaatilised tehted, toetatud funktsioonid, konstandid `pi` ja `e` ning `ans`.

Parser lükkab tagasi tundmatud nimed, atribuutidele ligipääsu, suvalised funktsioonikutsed ja muu mittetoetatud Pythoni süntaksi. Kui funktsiooni või tuntud nime kirjapilt on piisavalt lähedane, pakub kalkulaator parandust.

## 🧪 Testid

Projektis on unit-testid nii kalkulaatori arvutusloogika kui ka AST-põhise avaldiste parseri jaoks. Testid kontrollivad muu hulgas tehete järjekorda, sulge, `ans`-i, funktsioone, konstante, koma ja punktiga kümnendarve, `x`, `×` ja `÷` sümboleid koos tavaliste `*` ja `/` märkidega, implitsiitset korrutamist, `^` astendamist, kalkulaatori-stiilis protsentide liitmist ja lahutamist, protsentidega korrutamist, jäägitehet, nulliga jagamist, kirjavigade soovitusi funktsioonidele, nimedele ja käskudele, teemakohast abi, `undo`, `clear` ja `clear history` käitumist, täpsemaid süntaksiveateateid, funktsioonide argumentide arvu ja keelatud sisendeid.

```bash
python -m unittest discover -s tests -v
```

## 🔒 Turvalisus ja automaatika

- CodeQL kontrollib koodi turvaprobleemide suhtes.
- Dependabot kontrollib GitHub Actionsi uuendusi kord nädalas.
- `.gitignore` hoiab ajutised Pythoni ja tööriistade failid repost väljas.

## ⚠️ Vigade käsitlemine

Kalkulaator kontrollib muu hulgas nulliga jagamist, vigaseid avaldisi, negatiivse arvu ruutjuurt, vigast logaritmi, tundmatuid nimesid, funktsioonide argumentide arvu ning mittetoetatud süntaksit.

Süntaksivigade puhul proovib kalkulaator öelda, mis täpselt valesti läks. Näiteks puuduva või üleliigse sulu korral nimetab ta sulu probleemi ning järjestikuste vigaste tehtemärkide korral näitab probleemseid märke. Muude süntaksivigade puhul kuvatakse võimalusel vea positsioon.

Levinud kirjavigade puhul pakub kalkulaator parandust ainult siis, kui sisend on piisavalt sarnane mõne toetatud nime või funktsiooniga:

```text
> sqr(9)
Error: tundmatu funktsioon 'sqr'. Kas mõtlesid 'sqrt'?

> pii * 2
Error: tundmatu nimi 'pii'. Kas mõtlesid 'pi'?

> banana + 1
Error: tundmatu nimi 'banana'.

> histroy
Tundmatu käsk 'histroy'. Kas mõtlesid 'history'?

> cler history
Tundmatu käsk 'cler history'. Kas mõtlesid 'clear history'?
```

## 🐛 Issues ja ideed

Kui leiad vea või sul on idee, kuidas kalkulaatorit paremaks teha, [ava uus issue](https://github.com/kodaniq/Kalkulaator/issues/new/choose).

## 🤝 Contributing

Parandused ja uued ideed on teretulnud. Täpsemad juhised leiad failist [CONTRIBUTING.md](CONTRIBUTING.md).

## 📄 Litsents

Projekt on avaldatud [MIT litsentsi](LICENSE) all.
