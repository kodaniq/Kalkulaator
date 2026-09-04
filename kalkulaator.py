print("Kalkulaator")

while True:
    arv1 = float(input("Mis on sinu esimene arv? "))
    tehe = input("Mis tehet tahad teha? (+, -, *, /): ")
    arv2 = float(input("Mis on sinu teine arv? "))

    if tehe == "+":
        print("Vastus:", arv1 + arv2)

    elif tehe == "-":
        print("Vastus:", arv1 - arv2)

    elif tehe == "*":
        print("Vastus:", arv1 * arv2)

    elif tehe == "/":
        if arv2 != 0:
            print("Vastus:", arv1 / arv2)
        else:
            print("Nulliga ei saa jagada ")

    else:
        print("Sellist tehet ei ole arvutada isegi ju!")

    print("Palun tee nyyd jargmine arvutus  ")