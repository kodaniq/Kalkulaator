import ast
import difflib
import math
import operator
import re

COMMANDS = ("help", "history", "clear")
CONSTANTS = {
    "pi": math.pi,
    "e": math.e,
}
BINARY_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
}
UNARY_OPERATORS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}
FUNCTIONS = ("sqrt", "abs", "sin", "cos", "tan", "log")
KNOWN_NAMES = (*FUNCTIONS, *CONSTANTS, "ans")


def suggestion(name, choices):
    """Pakub ainult piisavalt sarnase kirjavea korral parandust."""
    matches = difflib.get_close_matches(name, choices, n=1, cutoff=0.7)
    return matches[0] if matches else None


def calculate(arv1, tehe, arv2=None):
    """Arvutab ühe toetatud tehte."""
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


def evaluate_node(node, ans):
    """Arvutab ainult kalkulaatori poolt lubatud AST-sõlmed."""
    if isinstance(node, ast.Constant):
        if isinstance(node.value, bool) or not isinstance(node.value, (int, float)):
            raise ValueError("lubatud on ainult arvud.")
        return node.value

    if isinstance(node, ast.Name):
        if node.id == "ans":
            if ans is None:
                raise ValueError("eelmist vastust veel ei ole.")
            return ans
        if node.id in CONSTANTS:
            return CONSTANTS[node.id]
        guessed = suggestion(node.id, KNOWN_NAMES)
        message = f"tundmatu nimi '{node.id}'."
        if guessed:
            message += f" Kas mõtlesid '{guessed}'?"
        raise ValueError(message)

    if isinstance(node, ast.BinOp) and type(node.op) in BINARY_OPERATORS:
        left = evaluate_node(node.left, ans)
        right = evaluate_node(node.right, ans)
        if isinstance(node.op, (ast.Div, ast.Mod)) and right == 0:
            raise ValueError("nulliga ei saa jagada ega jääki arvutada.")
        try:
            return BINARY_OPERATORS[type(node.op)](left, right)
        except (OverflowError, ZeroDivisionError) as error:
            raise ValueError("seda avaldist ei saa arvutada.") from error

    if isinstance(node, ast.UnaryOp) and type(node.op) in UNARY_OPERATORS:
        return UNARY_OPERATORS[type(node.op)](evaluate_node(node.operand, ans))

    if isinstance(node, ast.Call):
        if not isinstance(node.func, ast.Name):
            raise ValueError("tundmatu funktsioon.")

        function_name = node.func.id
        if function_name not in FUNCTIONS:
            guessed = suggestion(function_name, FUNCTIONS)
            message = f"tundmatu funktsioon '{function_name}'."
            if guessed:
                message += f" Kas mõtlesid '{guessed}'?"
            raise ValueError(message)

        if len(node.args) != 1 or node.keywords:
            raise ValueError(f"funktsioon '{function_name}' vajab täpselt ühte argumenti.")

        return calculate(evaluate_node(node.args[0], ans), function_name)

    raise ValueError("avaldis sisaldab mittetoetatud süntaksit.")


def normalize_expression(expression):
    """Teisendab kasutajasõbraliku süntaksi AST-le sobivaks."""
    expression = expression.strip().replace("^", "**")

    # Postfix-protsent: 15% -> (15 / 100), samal ajal jääb 10 % 3 jäägitehteks.
    percent_pattern = r"(\b(?:\d+(?:\.\d+)?|ans|pi|e)|\))\s*%(?=\s*(?:$|[+\-*/)]))"
    while re.search(percent_pattern, expression):
        expression = re.sub(percent_pattern, r"(\1 / 100)", expression)

    parts = expression.split(maxsplit=1)
    if len(parts) == 2 and parts[0] in FUNCTIONS:
        return f"{parts[0]}({parts[1]})"
    return expression


def parse_expression(expression, ans):
    """Parsib ja arvutab avaldise turvaliselt ilma eval()-ita."""
    normalized = normalize_expression(expression.lower())
    try:
        tree = ast.parse(normalized, mode="eval")
    except SyntaxError as error:
        raise ValueError("vigane avaldis. Abi saamiseks kirjuta help.") from error

    try:
        result = evaluate_node(tree.body, ans)
    except (ValueError, TypeError) as error:
        raise ValueError(str(error)) from error

    if not isinstance(result, (int, float)) or isinstance(result, bool):
        raise ValueError("tulemus peab olema arv.")

    return result


def show_help():
    print("\n--- Abi ---")
    print("Näited:")
    print("  5 + 3 * 2")
    print("  (5 + 3) * 2")
    print("  2 ^ 3 + 4")
    print("  ans / 2 + 7")
    print("  sqrt 144")
    print("  sin(30) + cos(60)")
    print("  2 * pi")
    print("  200 * 15%")
    print("\nTehted: +, -, *, /, ^, **, %")
    print("Protsent: näiteks 200 * 15%")
    print("Funktsioonid: sqrt, abs, sin, cos, tan, log")
    print("Konstandid: pi, e")
    print("sin, cos ja tan kasutavad kraade.")
    print("ans kasutab eelmise arvutuse vastust.")
    print("Käsud: help, history, clear")


def show_history(history):
    print("\n--- Arvutuste ajalugu ---")
    if not history:
        print("Ajalugu on tühi.")
        return
    for number, calculation in enumerate(history, start=1):
        print(f"{number}. {calculation}")


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
    print("Sisesta avaldis, näiteks: (5 + 3) * 2 või sin(30) + cos(60)")
    print("Käsud: help, history, clear")

    while True:
        expression = input("\n> ").strip()

        if expression.lower() in COMMANDS:
            handle_command(expression.lower(), history)
            continue

        if not expression:
            continue

        try:
            result = parse_expression(expression, ans)
            ans = result
            formatted = format_number(result)
            print("Vastus:", formatted)
            history.append(f"{expression} = {formatted}")
        except ValueError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
