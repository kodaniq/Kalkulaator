# 🧮 Kalkulaator

[![CodeQL](https://github.com/kodaniq/Kalkulaator/actions/workflows/codeql.yml/badge.svg)](https://github.com/kodaniq/Kalkulaator/actions/workflows/codeql.yml)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Lihtne Pythonis kirjutatud käsurea kalkulaator, mis toetab põhilisi ja teaduslikke matemaatilisi tehteid, arvutuste ajalugu ning abikäsku.

## ✨ Funktsioonid

- Liitmine, lahutamine, korrutamine ja jagamine
- Astendamine ja jäägi leidmine
- Ruutjuur ja absoluutväärtus
- Trigonomeetria: `sin`, `cos` ja `tan` kraadides
- Kümnendlogaritm (`log`)
- `ans` eelmise vastuse kasutamiseks järgmises arvutuses
- Arvutuste ajalugu
- `help`, `history` ja `clear` käsud
- Vigaste sisendite kontroll
- Täisarvulised vastused kuvatakse ilma üleliigse `.0` lõputa

## 📋 Nõuded

- Python 3.10 või uuem
- Väliseid teeke pole vaja

## ▶️ Käivitamine

```bash
python kalkulaator.py
```

Mõnes süsteemis:

```bash
python3 kalkulaator.py
```

## 💻 Kasutamise näide

```text
Kalkulaator
Tehted: +, -, *, /, **, %, sqrt, abs, sin, cos, tan, log
Käsud: help, history, clear
Eelmise vastuse kasutamiseks kirjuta ans.

Mis on sinu esimene arv? 5
Mis tehet tahad teha? (+, -, *, /, **, %, sqrt, abs, sin, cos, tan, log): +
Mis on sinu teine arv? 3
Vastus: 8

Mis on sinu esimene arv? ans
Mis tehet tahad teha? (+, -, *, /, **, %, sqrt, abs, sin, cos, tan, log): *
Mis on sinu teine arv? 2
Vastus: 16
```

## ➗ Tehted

| Märk | Tähendus | Näide |
| --- | --- | --- |
| `+` | Liitmine | 5 + 3 = 8 |
| `-` | Lahutamine | 5 - 3 = 2 |
| `*` | Korrutamine | 5 * 3 = 15 |
| `/` | Jagamine | 6 / 3 = 2 |
| `**` | Astendamine | 2 ** 3 = 8 |
| `%` | Jäägi leidmine | 10 % 3 = 1 |
| `sqrt` | Ruutjuur | sqrt 9 = 3 |
| `abs` | Absoluutväärtus | abs -5 = 5 |
| `sin` | Siinus kraadides | sin 90 = 1 |
| `cos` | Koosinus kraadides | cos 180 = -1 |
| `tan` | Tangens kraadides | tan 45 ≈ 1 |
| `log` | Kümnendlogaritm | log 100 = 2 |

## ⌨️ Käsud

| Käsk | Tegevus |
| --- | --- |
| `help` | Näitab saadaolevaid tehteid ja käske |
| `history` | Näitab selle käivituse jooksul tehtud arvutusi |
| `clear` | Tühjendab arvutuste ajaloo |
| `ans` | Kasutab eelmist vastust arvu asemel |

`ans` töötab nii esimese kui ka teise arvu asemel. Kui eelmist vastust veel pole, annab kalkulaator veateate.

## 🕘 Arvutuste ajalugu

Ajalugu hoitakse ainult programmi töötamise ajal ja seda saab tühjendada käsuga `clear`.

## 🧪 Testid

Projektis on unit-testid kalkulaatori arvutusloogika jaoks. Neid saab lokaalselt käivitada:

```bash
python -m unittest discover -s tests -v
```

## 🔒 Turvalisus ja automaatika

- CodeQL kontrollib koodi turvaprobleemide suhtes.
- Dependabot kontrollib GitHub Actionsi uuendusi kord nädalas.
- `.gitignore` hoiab ajutised Pythoni ja tööriistade failid repost väljas.

## ⚠️ Vigade käsitlemine

Kalkulaator kontrollib muu hulgas nulliga jagamist, vigaseid sisendeid, negatiivse arvu ruutjuurt, vigast logaritmi ja tundmatuid tehtemärke.

## 🐛 Issues ja ideed

Kui leiad vea või sul on idee, kuidas kalkulaatorit paremaks teha, [ava uus issue](https://github.com/kodaniq/Kalkulaator/issues/new/choose).

Saad valida interaktiivse **Bug report** või **Feature request** vormi.

## 🤝 Contributing

Parandused ja uued ideed on teretulnud. Täpsemad juhised leiad failist [CONTRIBUTING.md](CONTRIBUTING.md).

## 📄 Litsents

Projekt on avaldatud [MIT litsentsi](LICENSE) all.
