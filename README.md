# 🧮 Kalkulaator

[![Tests](https://github.com/kodaniq/Kalkulaator/actions/workflows/tests.yml/badge.svg)](https://github.com/kodaniq/Kalkulaator/actions/workflows/tests.yml)
[![CodeQL](https://github.com/kodaniq/Kalkulaator/actions/workflows/codeql.yml/badge.svg)](https://github.com/kodaniq/Kalkulaator/actions/workflows/codeql.yml)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Lihtne Pythonis kirjutatud käsurea kalkulaator, mis toetab põhilisi matemaatilisi tehteid, ruutjuurt ja vigaste sisendite kontrollimist.

## ✨ Funktsioonid

- Liitmine, lahutamine, korrutamine ja jagamine
- Astendamine
- Jäägi leidmine
- Ruutjuure arvutamine
- Vigaste sisendite kontroll
- Programmist väljumine käsuga `q` või `exit`

## 📋 Nõuded

- Python 3.10 või uuem
- Kalkulaatori kasutamiseks pole väliseid teeke vaja

## ▶️ Käivitamine

Klooni või laadi projekt alla ning käivita terminalis:

```bash
python kalkulaator.py
```

Mõnes süsteemis võib olla vaja kasutada:

```bash
python3 kalkulaator.py
```

## 💻 Kasutamise näide

```text
Kalkulaator
Tehted: +, -, *, /, **, %, sqrt
Väljumiseks kirjuta q või exit.

Mis on sinu esimene arv? 5
Mis tehet tahad teha? (+, -, *, /, **, %, sqrt): +
Mis on sinu teine arv? 3
Vastus: 8.0
```

## ➗ Tehtemärgid

| Märk | Tähendus | Näide |
| --- | --- | --- |
| `+` | Liitmine | 5 + 3 = 8 |
| `-` | Lahutamine | 5 - 3 = 2 |
| `*` | Korrutamine | 5 * 3 = 15 |
| `/` | Jagamine | 6 / 3 = 2 |
| `**` | Astendamine | 2 ** 3 = 8 |
| `%` | Jäägi leidmine | 10 % 3 = 1 |
| `sqrt` | Ruutjuur | sqrt 9 = 3 |

## 🧪 Testid ja koodi kvaliteet

Projektis on automaatsed unit-testid ning GitHub Actions kontrollib iga pushi ja pull requesti puhul:

- teste Python 3.10–3.13 versioonidega;
- test coverage'it;
- koodi kvaliteeti Ruffiga.

Lokaalselt saad kontrollid käivitada näiteks nii:

```bash
python -m pip install ruff coverage
ruff check .
coverage run -m unittest discover -s tests -v
coverage report
```

## 🔒 Turvalisus ja automaatika

- CodeQL kontrollib koodi turvaprobleemide suhtes.
- Dependabot kontrollib GitHub Actionsi uuendusi kord nädalas.
- `.gitignore` hoiab ajutised Pythoni ja tööriistade failid repost väljas.

## ⚠️ Vigade käsitlemine

Kalkulaator kontrollib vigaseid sisendeid, näiteks:

- Teksti sisestamine arvu asemel
- Nulliga jagamine
- Nulliga jäägi arvutamine
- Negatiivse arvu ruutjuure arvutamine
- Tundmatu tehtemärgi sisestamine

## 🚪 Programmist väljumine

Programmist saab väljuda, sisestades `q` või `exit`.

## 🐛 Issues ja ideed

Kui leiad vea või sul on idee, kuidas kalkulaatorit paremaks teha, [ava uus issue](https://github.com/kodaniq/Kalkulaator/issues/new/choose).

Saad valida interaktiivse **Bug report** või **Feature request** vormi. Tühjad issue'd on välja lülitatud, et vajalik info saaks kohe kaasa.

## 🤝 Contributing

Parandused ja uued ideed on teretulnud. Täpsemad juhised leiad failist [CONTRIBUTING.md](CONTRIBUTING.md).

## 📄 Litsents

Projekt on avaldatud [MIT litsentsi](LICENSE) all.
