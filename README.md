# 🧮 Kalkulaator

Lihtne Pythonis kirjutatud käsurea kalkulaator, mis toetab põhilisi matemaatilisi tehteid, ruutjuurt ja vigaste sisendite kontrollimist.

## ✨ Funktsioonid

- Liitmine, lahutamine, korrutamine ja jagamine
- Astendamine
- Jäägi leidmine
- Ruutjuure arvutamine
- Vigaste sisendite kontroll
- Programmist väljumine käsuga `q` või `exit`

## 📋 Nõuded

- Python 3
- Väliseid teeke pole vaja

Kalkulaator kasutab ainult Pythoni standardteeki `math`.

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

## ⚠️ Vigade käsitlemine

Kalkulaator kontrollib vigaseid sisendeid, näiteks:

- Teksti sisestamine arvu asemel
- Nulliga jagamine
- Nulliga jäägi arvutamine
- Negatiivse arvu ruutjuure arvutamine
- Tundmatu tehtemärgi sisestamine

## 🚪 Programmist väljumine

Programmist saab väljuda, sisestades `q` või `exit`.

## 🐛 Issues / vigadest teatamine

Kui leiad vea või sul on idee, kuidas kalkulaatorit paremaks teha, [ava uus issue](https://github.com/kodaniq/Kalkulaator/issues/new).

Palun kirjelda võimalusel:

- mida tegid;
- mida ootasid;
- mis tegelikult juhtus.

## 🤝 Contributing

Parandused ja uued ideed on teretulnud. Võid avada issue või saata pull requesti.
