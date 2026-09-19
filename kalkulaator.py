import math


def calculate(arv1, tehe, arv2=None):
    """Arvutab tulemuse antud arvude ja tehtemärgi põhjal."""
    if tehe == "sqrt":
        if arv1 < 0:
            raise ValueError("negatiivsest arvust ei saa ruutjuurt võtta.")
        return math.sqrt(arv1)

    if tehe == "+":
        return arv1 + arv2
    if tehe == "-":
        return arv1 - arv2
    if tehe == "*":
        return arv1 * arv2
    if tehe == "/":
        if arv2 == 0:
            raise ValueError("nulliga ei saa jagada.")
        return arv1 / arv2
    if tehe == "**":
        return arv1**arv2
    if tehe == "%":
        if arv2 == 0:
            raise ValueError("nulliga ei saa jääki arvutada.")
        return arv1 % arv2

    raise ValueError("sellist tehet ei ole.")


def main():
    print("Kalkulaator")
    print("Tehted: +, -, *, /, **, %, sqrt")
    print("Väljumiseks kirjuta q või exit.")

    while True:
        esimene = input("\nMis on sinu esimene arv? ").strip()

        if esimene.lower() in ("q", "exit"):
            print("Headaega!")
            break

        try:
            arv1 = float(esimene)
        except ValueError:
            print("Error: palun sisesta arv.")
            continue

        tehe = input(
            "Mis tehet tahad teha? (+, -, *, /, **, %, sqrt): "
        ).strip().lower()

        if tehe in ("q", "exit"):
            print("Headaega!")
            break

        if tehe not in ("+", "-", "*", "/", "**", "%", "sqrt"):
            print("Error: sellist tehet ei ole.")
            continue

        if tehe == "sqrt":
            try:
                print("Vastus:", calculate(arv1, tehe))
            except ValueError as error:
                print("Error:", error)
            continue

        teine = input("Mis on sinu teine arv? ").strip()

        if teine.lower() in ("q", "exit"):
            print("Headaega!")
            break

        try:
            arv2 = float(teine)
        except ValueError:
            print("Error: palun sisesta arv.")
            continue

        try:
            print("Vastus:", calculate(arv1, tehe, arv2))
        except ValueError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
