import math

print("🧮 Kalkulaator v2")
print("Tehted: +, -, *, /, **, %, sqrt")
print("Väljumiseks kirjuta q või exit.\n")

while True:
    esimene = input("👉 Mis on sinu esimene arv? ").strip()

    if esimene.lower() in ("q", "exit"):
        print("👋 Tsau! Kalkulaator pandi kinni.")
        break

    try:
        arv1 = float(esimene)
    except ValueError:
        print("❌ See pole arv 😭 Proovi uuesti.\n")
        continue

    tehe = input("⚙️ Mis tehet tahad teha? (+, -, *, /, **, %, sqrt): ").strip().lower()

    if tehe in ("q", "exit"):
        print("👋 Tsau! Kalkulaator pandi kinni.")
        break

    if tehe == "sqrt":
        if arv1 < 0:
            print("❌ Negatiivsest arvust ei saa siin ruutjuurt võtta 😭")
        else:
            print("✅ Vastus:", math.sqrt(arv1))
        print("\n🔄 Teeme järgmise arvutuse!\n")
        continue

    if tehe not in ("+", "-", "*", "/", "**", "%"):
        print("❌ Sellist tehet ma ei tunne 💀\n")
        continue

    teine = input("👉 Mis on sinu teine arv? ").strip()

    if teine.lower() in ("q", "exit"):
        print("👋 Tsau! Kalkulaator pandi kinni.")
        break

    try:
        arv2 = float(teine)
    except ValueError:
        print("❌ See pole arv 😭 Proovi uuesti.\n")
        continue

    if tehe == "+":
        vastus = arv1 + arv2
    elif tehe == "-":
        vastus = arv1 - arv2
    elif tehe == "*":
        vastus = arv1 * arv2
    elif tehe == "/":
        if arv2 == 0:
            print("❌ Nulliga ei saa jagada gng 💀")
            print("\n🔄 Teeme järgmise arvutuse!\n")
            continue
        vastus = arv1 / arv2
    elif tehe == "**":
        vastus = arv1 ** arv2
    else:
        if arv2 == 0:
            print("❌ Nulliga ei saa jääki arvutada 💀")
            print("\n🔄 Teeme järgmise arvutuse!\n")
            continue
        vastus = arv1 % arv2

    print("✅ Vastus:", vastus)
    print("\n🔄 Teeme järgmise arvutuse!\n")
