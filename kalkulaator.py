print("Kalkulaator")
print("Tehted: +, -, *, /")
print("Väljumiseks kirjuta q.\n")

while True:
    esimene = input("Mis on sinu esimene arv? ").strip()

    if esimene.lower() == "q":
        print("Tsau!")
        break

    try:
        arv1 = float(esimene)
    except ValueError:
        print("Palun sisesta arv.\n")
        continue

    tehe = input("Mis tehet tahad teha? (+, -, *, /): ").strip()

    if tehe.lower() == "q":
        print("Tsau!")
        break

    if tehe not in ("+", "-", "*", "/"):
        print("Sellist tehet ei ole.\n")
        continue

    teine = input("Mis on sinu teine arv? ").strip()

    if teine.lower() == "q":
        print("Tsau!")
        break

    try:
        arv2 = float(teine)
    except ValueError:
        print("Palun sisesta arv.\n")
        continue

    if tehe == "+":
        vastus = arv1 + arv2
    elif tehe == "-":
        vastus = arv1 - arv2
    elif tehe == "*":
        vastus = arv1 * arv2
    else:
        if arv2 == 0:
            print("Nulliga ei saa jagada.\n")
            continue
        vastus = arv1 / arv2

    print("Vastus:", vastus)
    print()
