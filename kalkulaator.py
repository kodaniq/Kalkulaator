import math

UNARY_OPERATIONS = ("sqrt", "abs", "sin", "cos", "tan", "log")
OPERATIONS = ("+", "-", "*", "/", "**", "%", *UNARY_OPERATIONS)
COMMANDS = ("help", "history", "clear")


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


def format_number(number):
    """Kuvab täisarvulise tulemuse ilma .0 lõputa."""
    if isinstance(number, float) and number.is_integer():
        return str(int(number))
    return f"{number:.10g}" if isinstance(number, float) else str(number)


def show_help():
    print("\n--- Abi ---")
    print("+     liitmine")
    print("-     lahutamine")
    print("*     korrutamine")
    print("/     jagamine")
    print("**    astendamine")
    print("%     jäägi leidmine")
    print("sqrt  ruutjuur")
    print("abs   absoluutväärtus")
    print("sin   siinus kraadides")
    print("cos   koosinus kraadides")
    print("tan   tangens kraadides")
    print("log   kümnendlogaritm")
    print("\nKäsud: help, history, clear")


def show_history(history):
    print("\n--- Arvutuste ajalugu ---")
    if not history:
        print("Ajalugu on tühi.")
        return
    for calculation in history:
        print(calculation)


def handle_command(command, history):
    if command == "help":
        show_help()
    elif command == "history":
        show_history(history)
    elif command == "clear":
        history.clear()
        print("Arvutuste ajalugu tühjendatud.")


def main():
    history = []

    print("Kalkulaator")
    print("Tehted: +, -, *, /, **, %, sqrt, abs, sin, cos, tan, log")
    print("Käsud: help, history, clear")
    print("sin, cos ja tan kasutavad kraade. log on kümnendlogaritm.")

    while True:
        esimene = input("\nMis on sinu esimene arv? ").strip().lower()

        if esimene in COMMANDS:
            handle_command(esimene, history)
            continue

        try:
            arv1 = float(esimene)
        except ValueError:
            print("Error: palun sisesta arv või käsk help.")
            continue

        tehe = input(
            "Mis tehet tahad teha? "
            "(+, -, *, /, **, %, sqrt, abs, sin, cos, tan, log): "
        ).strip().lower()

        if tehe in COMMANDS:
            handle_command(tehe, history)
            continue

        if tehe not in OPERATIONS:
            print("Error: sellist tehet ei ole.")
            continue

        if tehe in UNARY_OPERATIONS:
            try:
                vastus = calculate(arv1, tehe)
                formatted = format_number(vastus)
                print("Vastus:", formatted)
                history.append(f"{tehe} {format_number(arv1)} = {formatted}")
            except ValueError as error:
                print("Error:", error)
            continue

        teine = input("Mis on sinu teine arv? ").strip().lower()

        if teine in COMMANDS:
            handle_command(teine, history)
            continue

        try:
            arv2 = float(teine)
        except ValueError:
            print("Error: palun sisesta arv või käsk help.")
            continue

        try:
            vastus = calculate(arv1, tehe, arv2)
            formatted = format_number(vastus)
            print("Vastus:", formatted)
            history.append(
                f"{format_number(arv1)} {tehe} {format_number(arv2)} = {formatted}"
            )
        except ValueError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
