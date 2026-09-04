import math

print("Kalkulaator")
print("Tehted: +, -, *, /, **, %, sqrt")
print("Väljumiseks kirjuta q või exit.")

while True:
    esimene = input("\nMis on sinu esimene arv? ").strip()

    if esimene.lower() in ("q", "exit"):
        print("Tsau!")
        break

    try:
        arv1 = float(esimene)
    except ValueError:
        print("Error: palun sisesta arv.")
        continue

    tehe = input("Mis tehet tahad teha? (+, -, *, /, **, %, sqrt): ").strip().lower()

    if tehe in ("q", "exit"):
        print("Tsau!")
        break

    if tehe == "sqrt":
        if arv1 < 0:
            print("Error: negatiivsest arvust ei saa ruutjuurt võtta.")
        else:
            print("Vastus:", math.sqrt(arv1))
        continue

    if tehe not in ("+", "-", "*", "/", "**", "%"):
        print("Error: sellist tehet ei ole.")
        continue

    teine = input("Mis on sinu teine arv? ").strip()

    if teine.lower() in ("q", "exit"):
        print("Tsau!")
        break

    try:
        arv2 = float(teine)
    except ValueError:
        print("Error: palun sisesta arv.")
        continue

    if tehe == "+":
        vastus = arv1 + arv2

    elif tehe == "-":
        vastus = arv1 - arv2

    elif tehe == "*":
        vastus = arv1 * arv2

    elif tehe == "/":
        if arv2 == 0:
            print("Error: nulliga ei saa jagada.")
            continue
        vastus = arv1 / arv2

    elif tehe == "**":
        vastus = arv1 ** arv2

    elif tehe == "%":
        if arv2 == 0:
            print("Error: nulliga ei saa jääki arvutada.")
            continue
        vastus = arv1 % arv2

    print("Vastus:", vastus) 
