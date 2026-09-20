# 🧮 Kalkulaator

[![CodeQL](https://github.com/kodaniq/Kalkulaator/actions/workflows/codeql.yml/badge.svg)](https://github.com/kodaniq/Kalkulaator/actions/workflows/codeql.yml)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Pythonis kirjutatud käsurea kalkulaator, mis toetab mitme tehtega avaldisi, sulge, teaduslikke funktsioone, matemaatilisi konstante ja arvutuste ajalugu.

## ✨ Funktsioonid

- Mitu tehet ühes avaldises
- Õige tehete järjekord
- Sulud
- Liitmine, lahutamine, korrutamine, jagamine, astendamine ja jääk
- `sqrt`, `abs`, `sin`, `cos`, `tan` ja `log`
- Matemaatilised konstandid `pi` ja `e`
- `ans` eelmise vastuse kasutamiseks
- `help`, `history` ja `clear`
- Vigaste sisendite kontroll
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
Käsud: help, history, clear

> 5 + 3 * 2
Vastus: 11

> (5 + 3) * 2
Vastus: 16

> 2 ** 3 + 4
Vastus: 12

> ans / 2 + 7
Vastus: 13

> sin(30) + cos(60)
Vastus: 1

> 2 * pi
Vastus: 6.283185307
```

Tühikud pole kohustuslikud: nii `5+3` kui ka `5 + 3` töötavad.

## ➗ Tehted ja funktsioonid

| Süntaks | Tähendus | Näide |
| --- | --- | --- |
| `+` | Liitmine | `5 + 3` → 8 |
| `-` | Lahutamine | `5 - 3` → 2 |
| `*` | Korrutamine | `5 * 3` → 15 |
| `/` | Jagamine | `6 / 3` → 2 |
| `**` | Astendamine | `2 ** 3` → 8 |
| `%` | Jäägi leidmine | `10 % 3` → 1 |
| `sqrt(x)` | Ruutjuur | `sqrt(9)` → 3 |
| `abs(x)` | Absoluutväärtus | `abs(-5)` → 5 |
| `sin(x)` | Siinus kraadides | `sin(90)` → 1 |
| `cos(x)` | Koosinus kraadides | `cos(180)` → -1 |
| `tan(x)` | Tangens kraadides | `tan(45)` → 1 |
| `log(x)` | Kümnendlogaritm | `log(100)` → 2 |

Lihtsad funktsioonid töötavad ka ilma sulgudeta, näiteks `sqrt 144`.

## 🔢 Konstandid

| Konstant | Tähendus | Näide |
| --- | --- | --- |
| `pi` | π | `2 * pi` → 6.283185307 |
| `e` | Euleri arv | `e ** 2` → 7.389056099 |

Konstante saab kasutada avaldistes samamoodi nagu tavalisi arve. Trigonomeetrilised funktsioonid `sin`, `cos` ja `tan` kasutavad endiselt kraade.

## ⌨️ Käsud

| Käsk | Tegevus |
| --- | --- |
| `help` | Näitab kasutusabi |
| `history` | Näitab selle käivituse jooksul tehtud arvutusi |
| `clear` | Tühjendab arvutuste ajaloo |
| `ans` | Kasutab avaldises eelmist vastust |

## 🕘 Arvutuste ajalugu

`history` näitab selle käivituse jooksul tehtud avaldisi ja vastuseid. Ajalugu saab tühjendada käsuga `clear`.

## 🔐 Avaldiste turvalisus

Kalkulaator ei kasuta sisendi arvutamiseks `eval()`-i. Avaldis parsitakse Pythoni AST abil ning lubatud on ainult numbrid, kalkulaatori matemaatilised tehted, toetatud funktsioonid, konstandid `pi` ja `e` ning `ans`.

Parser lükkab tagasi tundmatud nimed, atribuutidele ligipääsu, suvalised funktsioonikutsed ja muu mittetoetatud Pythoni süntaksi.

## 🧪 Testid

Projektis on unit-testid nii kalkulaatori arvutusloogika kui ka AST-põhise avaldiste parseri jaoks. Testid kontrollivad muu hulgas tehete järjekorda, sulge, `ans`-i, funktsioone, konstante, nulliga jagamist ja keelatud sisendeid.

```bash
python -m unittest discover -s tests -v
```

## 🔒 Turvalisus ja automaatika

- CodeQL kontrollib koodi turvaprobleemide suhtes.
- Dependabot kontrollib GitHub Actionsi uuendusi kord nädalas.
- `.gitignore` hoiab ajutised Pythoni ja tööriistade failid repost väljas.

## ⚠️ Vigade käsitlemine

Kalkulaator kontrollib muu hulgas nulliga jagamist, vigaseid avaldisi, negatiivse arvu ruutjuurt, vigast logaritmi, tundmatuid nimesid ning mittetoetatud süntaksit.

## 🐛 Issues ja ideed

Kui leiad vea või sul on idee, kuidas kalkulaatorit paremaks teha, [ava uus issue](https://github.com/kodaniq/Kalkulaator/issues/new/choose).

## 🤝 Contributing

Parandused ja uued ideed on teretulnud. Täpsemad juhised leiad failist [CONTRIBUTING.md](CONTRIBUTING.md).

## 📄 Litsents

Projekt on avaldatud [MIT litsentsi](LICENSE) all.
