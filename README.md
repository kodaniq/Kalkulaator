# 🧮 Kalkulaator

[![CodeQL](https://github.com/kodaniq/Kalkulaator/actions/workflows/codeql.yml/badge.svg)](https://github.com/kodaniq/Kalkulaator/actions/workflows/codeql.yml)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Lihtne Pythonis kirjutatud käsurea kalkulaator, kus matemaatilise avaldise saab sisestada otse ühele reale.

## ✨ Funktsioonid

- Avaldised kujul `5 + 3`, `sqrt 9` või `ans * 10`
- Liitmine, lahutamine, korrutamine ja jagamine
- Astendamine ja jäägi leidmine
- Ruutjuur ja absoluutväärtus
- Trigonomeetria kraadides: `sin`, `cos`, `tan`
- Kümnendlogaritm (`log`)
- `ans` eelmise vastuse kasutamiseks
- Arvutuste ajalugu
- `help`, `history` ja `clear`
- Vigaste sisendite kontroll
- Avaldisi parsitakse ilma `eval()` kasutamata

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

## 💻 Kasutamine

```text
Kalkulaator
Sisesta avaldis, näiteks: 5 + 3, sqrt 9 või ans * 2
Käsud: help, history, clear

> 5 + 3
Vastus: 8

> ans * 10
Vastus: 80

> sqrt 144
Vastus: 12

> sin 90
Vastus: 1
```

Tehte osad eraldatakse tühikutega. Näiteks kirjuta `5 + 3`, mitte `5+3`.

## ➗ Tehted

| Märk | Tähendus | Näide |
| --- | --- | --- |
| `+` | Liitmine | `5 + 3` → 8 |
| `-` | Lahutamine | `5 - 3` → 2 |
| `*` | Korrutamine | `5 * 3` → 15 |
| `/` | Jagamine | `6 / 3` → 2 |
| `**` | Astendamine | `2 ** 3` → 8 |
| `%` | Jäägi leidmine | `10 % 3` → 1 |
| `sqrt` | Ruutjuur | `sqrt 9` → 3 |
| `abs` | Absoluutväärtus | `abs -5` → 5 |
| `sin` | Siinus kraadides | `sin 90` → 1 |
| `cos` | Koosinus kraadides | `cos 180` → -1 |
| `tan` | Tangens kraadides | `tan 45` → 1 |
| `log` | Kümnendlogaritm | `log 100` → 2 |

## ⌨️ Käsud

| Käsk | Tegevus |
| --- | --- |
| `help` | Näitab kasutusabi |
| `history` | Näitab selle käivituse jooksul tehtud arvutusi |
| `clear` | Tühjendab arvutuste ajaloo |
| `ans` | Kasutab avaldises eelmist vastust |

## 🕘 Arvutuste ajalugu

`history` näitab tehtud arvutusi:

```text
--- Arvutuste ajalugu ---
5 + 3 = 8
8 * 10 = 80
sqrt 144 = 12
```

Ajalugu hoitakse ainult programmi töötamise ajal.

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

Kalkulaator kontrollib muu hulgas nulliga jagamist, vigaseid sisendeid, negatiivse arvu ruutjuurt, vigast logaritmi ja tundmatuid avaldisi.

## 🐛 Issues ja ideed

Kui leiad vea või sul on idee, kuidas kalkulaatorit paremaks teha, [ava uus issue](https://github.com/kodaniq/Kalkulaator/issues/new/choose).

Saad valida interaktiivse **Bug report** või **Feature request** vormi.

## 🤝 Contributing

Parandused ja uued ideed on teretulnud. Täpsemad juhised leiad failist [CONTRIBUTING.md](CONTRIBUTING.md).

## 📄 Litsents

Projekt on avaldatud [MIT litsentsi](LICENSE) all.
