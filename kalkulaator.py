import math

UNARY_OPERATIONS = ("sqrt", "abs", "sin", "cos", "tan", "log")
OPERATIONS = ("+", "-", "*", "/", "**", "%", *UNARY_OPERATIONS)


def calculate(arv1, tehe, arv2=None):
    """Arvutab tulemuse antud arvude ja tehtemärgi põhjal."""
    if tehe == "sqrt":
        if arv1 < 0:
            raise ValueError("negatiivsest arvust ei saa ruutjuurt võtta.")
        return math.sqrt(arv1)
    if tehe == "abs":
        return abs(arv1)
    if tehe == "sin":
        return math.sin(math.radians(arv1))
    if tehe == "cos":
        return math.cos(math.radians(arv1))
    if tehe == "tan":
        return math.tan(math.radians(arv1))
    if tehe == "log":
        if arv1 <= 0:
            raise ValueError("logaritmi saab arvutada ainult positiivsest arvust.")
        return math.log10(arv1)

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
    print("Tehted: +, -, *, /, **, %, sqrt, abs, sin, cos, tan, log")
    print("sin, cos ja tan kasutavad kraade. log on kümnendlogaritm.")
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
            "Mis tehet tahad teha? "
            "(+, -, *, /, **, %, sqrt, abs, sin, cos, tan, log): "
        ).strip().lower()

        if tehe in ("q", "exit"):
            print("Headaega!")
            break

        if tehe not in OPERATIONS:
            print("Error: sellist tehet ei ole.")
            continue

        if tehe in UNARY_OPERATIONS:
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
