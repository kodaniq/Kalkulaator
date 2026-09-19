import math

UNARY_OPERATIONS = ("sqrt", "abs", "sin", "cos", "tan", "log")
BINARY_OPERATIONS = ("+", "-", "*", "/", "**", "%")
OPERATIONS = (*BINARY_OPERATIONS, *UNARY_OPERATIONS)
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


def parse_number(value, ans):
    """Teisendab sisendi arvuks või kasutab eelmist vastust."""
    if value == "ans":
        if ans is None:
            raise ValueError("eelmist vastust veel ei ole.")
        return ans
    try:
        return float(value)
    except ValueError as error:
        raise ValueError(f"'{value}' ei ole arv.") from error


def parse_expression(expression, ans):
    """Parsib lubatud kujul matemaatilise avaldise ilma eval()-ita."""
    parts = expression.lower().split()

    if len(parts) == 2 and parts[0] in UNARY_OPERATIONS:
        operation, value = parts
        number = parse_number(value, ans)
        result = calculate(number, operation)
        shown = f"{operation} {format_number(number)}"
        return result, shown

    if len(parts) == 3 and parts[1] in BINARY_OPERATIONS:
        first, operation, second = parts
        number1 = parse_number(first, ans)
        number2 = parse_number(second, ans)
        result = calculate(number1, operation, number2)
        shown = (
            f"{format_number(number1)} {operation} {format_number(number2)}"
        )
        return result, shown

    raise ValueError(
        "kasuta kuju '5 + 3' või 'sqrt 9'. Abi saamiseks kirjuta help."
    )


def show_help():
    print("\n--- Abi ---")
    print("Sisesta avaldis ühele reale, näiteks:")
    print("  5 + 3")
    print("  ans * 10")
    print("  sqrt 144")
    print("  sin 90")
    print("\nTehted: +, -, *, /, **, %, sqrt, abs, sin, cos, tan, log")
    print("ans kasutab eelmise arvutuse vastust.")
    print("Käsud: help, history, clear")


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
    ans = None

    print("Kalkulaator")
    print("Sisesta avaldis, näiteks: 5 + 3, sqrt 9 või ans * 2")
    print("Käsud: help, history, clear")

    while True:
        expression = input("\n> ").strip().lower()

        if expression in COMMANDS:
            handle_command(expression, history)
            continue

        if not expression:
            continue

        try:
            result, shown = parse_expression(expression, ans)
            ans = result
            formatted = format_number(result)
            print("Vastus:", formatted)
            history.append(f"{shown} = {formatted}")
        except ValueError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
