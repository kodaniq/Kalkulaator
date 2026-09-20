import ast
import difflib
import math
import operator
import os
import re

COMMANDS = ("help", "history", "clear", "clear history", "undo")
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


def command_suggestion(command):
    """Pakub käsu kirjavea korral parandust, aga ei sega tavalisi avaldisi."""
    if not command or any(char.isdigit() or char in "+-*/%^×÷()" for char in command):
        return None
    return suggestion(command, COMMANDS)


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
    expression = expression.strip().replace("×", "*").replace("÷", "/").replace("^", "**")

    # x või X töötab korrutusmärgina siis, kui see on arvutuslike väärtuste vahel.
    # Näiteks 2x(5+26), 5x3 ja (2+3)x4.
    expression = re.sub(r"(?<=[\d)])\s*[xX]\s*(?=(?:\d|\(|ans\b|pi\b|e\b|(?:sqrt|abs|sin|cos|tan|log)\b))", " * ", expression)

    # Eesti komakohad: 2,5 -> 2.5. Muud komad jäävad alles, et vigane süntaks
    # (nt mitme argumendiga funktsioon) ei muutuks kogemata teiseks avaldiseks.
    expression = re.sub(r"(?<=\d),(?=\d)", ".", expression)

    # Kalkulaatori-stiilis protsent liitmisel/lahutamisel:
    # 200 + 15% -> 200 + (200 * 15 / 100), 200 - 15% -> 170.
    relative_percent_pattern = r"(?P<base>(?:\d+(?:\.\d+)?|ans|pi|e))\s*(?P<op>[+\-])\s*(?P<pct>\d+(?:\.\d+)?)\s*%"
    while re.search(relative_percent_pattern, expression):
        expression = re.sub(
            relative_percent_pattern,
            lambda match: (
                f"{match.group('base')} {match.group('op')} "
                f"({match.group('base')} * {match.group('pct')} / 100)"
            ),
            expression,
        )

    # Muudel juhtudel on postfix-protsent lihtsalt sajandik:
    # 15% -> 0.15 ja 200 * 15% -> 30. Kahe arvu vahel olev 10 % 3 jääb modulo-tehteks.
    percent_pattern = r"(\b(?:\d+(?:\.\d+)?|ans|pi|e)|\))\s*%(?=\s*(?:$|[+\-*/)]))"
    while re.search(percent_pattern, expression):
        expression = re.sub(percent_pattern, r"(\1 / 100)", expression)

    parts = expression.split(maxsplit=1)
    if len(parts) == 2 and parts[0] in FUNCTIONS:
        expression = f"{parts[0]}({parts[1]})"

    # Implitsiitne korrutamine: 2pi, 2(3 + 4), 3sqrt(9), (2 + 3)(4 + 5).
    function_pattern = "|".join(FUNCTIONS)
    value_pattern = r"(?:\d+(?:\.\d+)?|ans|pi|e|\))"
    expression = re.sub(rf"({value_pattern})(?=\s*(?:{function_pattern})\s*\()", r"\1 * ", expression)
    expression = re.sub(rf"({value_pattern})(?=\s*\()", r"\1 * ", expression)
    expression = re.sub(r"(\))\s*(?=(?:\d|ans\b|pi\b|e\b))", r"\1 * ", expression)
    expression = re.sub(r"(\d+(?:\.\d+)?)\s*(?=(?:ans\b|pi\b|e\b))", r"\1 * ", expression)
    return expression


def syntax_error_message(expression, error):
    """Muudab Pythoni SyntaxError-i kasutajasõbralikumaks."""
    opening = expression.count("(")
    closing = expression.count(")")
    if opening > closing:
        return "sulgev ) on puudu."
    if closing > opening:
        return "üleliigne ) avaldises."

    operators = r"(?:\*\*|[+\-*/%])"
    match = re.search(rf"({operators})\s*({operators})(?!\*)", expression)
    if match:
        return f"ootamatu {match.group(2)} pärast {match.group(1)}."

    if error.offset:
        return f"vigane avaldis positsiooni {error.offset} juures. Abi saamiseks kirjuta help."
    return "vigane avaldis. Abi saamiseks kirjuta help."


def parse_expression(expression, ans):
    """Parsib ja arvutab avaldise turvaliselt ilma eval()-ita."""
    normalized = normalize_expression(expression.lower())
    try:
        tree = ast.parse(normalized, mode="eval")
    except SyntaxError as error:
        raise ValueError(syntax_error_message(normalized, error)) from error

    try:
        result = evaluate_node(tree.body, ans)
    except (ValueError, TypeError) as error:
        raise ValueError(str(error)) from error

    if not isinstance(result, (int, float)) or isinstance(result, bool):
        raise ValueError("tulemus peab olema arv.")

    return result


HELP_TOPICS = {
    "sqrt": ("sqrt(x) — leiab ruutjuure.", "Näide: sqrt(144) → 12"),
    "abs": ("abs(x) — leiab absoluutväärtuse.", "Näide: abs(-5) → 5"),
    "sin": ("sin(x) — leiab siinuse kraadides.", "Näide: sin(90) → 1"),
    "cos": ("cos(x) — leiab koosinuse kraadides.", "Näide: cos(180) → -1"),
    "tan": ("tan(x) — leiab tangensi kraadides.", "Näide: tan(45) → 1"),
    "log": ("log(x) — leiab kümnendlogaritmi.", "Näide: log(100) → 2"),
    "pi": ("pi — matemaatiline konstant π.", "Näide: 2 * pi → 6.283185307"),
    "e": ("e — Euleri arv.", "Näide: e ^ 2 → 7.389056099"),
    "ans": ("ans — eelmise arvutuse tulemus.", "Näide: ans / 2"),
    "%": ("15% — protsent; + ja - puhul arvestatakse protsenti eelnevast arvust.", "Näited: 200 + 15% → 230, 200 - 15% → 170, 200 * 15% → 30, 10 % 3 → 1"),
    "^": ("^ või ** — astendamine.", "Näide: 2 ^ 10 → 1024"),
    "history": ("history — näitab selle käivituse arvutuste ajalugu.",),
    "clear": ("clear — puhastab terminali ekraani.", "clear history — tühjendab arvutuste ajaloo."),
    "undo": ("undo — eemaldab viimase arvutuse ja taastab eelmise ans väärtuse.",),
}


def show_help(topic=None):
    if topic:
        topic = topic.lower()
        if topic in HELP_TOPICS:
            print(f"\n--- Abi: {topic} ---")
            for line in HELP_TOPICS[topic]:
                print(line)
            return

        guessed = suggestion(topic, HELP_TOPICS)
        if guessed:
            print(f"Tundmatu abiteema '{topic}'. Kas mõtlesid '{guessed}'?")
        else:
            print(f"Tundmatu abiteema '{topic}'.")
        return

    print("\n--- Abi ---")
    print("Näited:")
    print("  5 + 3 * 2")
    print("  2,5 + 1,5")
    print("  5 × 3")
    print("  2x(5 + 26) - 32")
    print("  10 ÷ 2")
    print("  (5 + 3) * 2")
    print("  2 ^ 3 + 4")
    print("  ans / 2 + 7")
    print("  sqrt 144")
    print("  sin(30) + cos(60)")
    print("  2pi")
    print("  200 + 15%")
    print("  200 * 15%")
    print("  2(3 + 4)")
    print("\nTehted: +, -, *, x, ×, /, ÷, ^, **, %")
    print("Funktsioonid: sqrt, abs, sin, cos, tan, log")
    print("Konstandid: pi, e")
    print("Korrutamisel võib * mõnikord ära jätta: 2pi, 2(3 + 4), 3sqrt(9)")
    print("Käsud: help, history, undo, clear, clear history")
    print("Täpsema abi jaoks: help <teema>, näiteks help sqrt")


def show_history(history):
    print("\n--- Arvutuste ajalugu ---")
    if not history:
        print("Ajalugu on tühi.")
        return
    for number, calculation in enumerate(history, start=1):
        expression, result = calculation
        print(f"{number}. {expression} = {format_number(result)}")


def clear_screen():
    """Puhastab terminali ekraani Windowsis, macOS-is ja Linuxis."""
    os.system("cls" if os.name == "nt" else "clear")


def undo(history):
    """Eemaldab viimase arvutuse ja tagastab eelmise ans väärtuse."""
    if not history:
        print("Midagi pole tagasi võtta.")
        return None

    history.pop()
    new_ans = history[-1][1] if history else None
    print("Eelmine arvutus eemaldatud.")
    print(f"ans = {format_number(new_ans)}" if new_ans is not None else "ans on tühi.")
    return new_ans


def handle_command(command, history):
    if command == "history":
        show_history(history)
    elif command == "clear":
        clear_screen()
    elif command == "clear history":
        history.clear()
        print("Arvutuste ajalugu tühjendatud.")


def main():
    history = []
    ans = None

    print("Kalkulaator")
    print("Sisesta avaldis, näiteks: (5 + 3) * 2 või sin(30) + cos(60)")
    print("Käsud: help, history, undo, clear, clear history")

    while True:
        expression = input("\n> ").strip()

        lowered = expression.lower()
        if lowered == "help" or lowered.startswith("help "):
            topic = expression.split(maxsplit=1)[1] if " " in expression else None
            show_help(topic)
            continue

        if lowered == "undo":
            ans = undo(history)
            continue

        if lowered in COMMANDS:
            handle_command(lowered, history)
            if lowered == "clear history":
                ans = None
            continue

        if not expression:
            continue

        guessed_command = command_suggestion(lowered)
        if guessed_command:
            print(f"Tundmatu käsk '{expression}'. Kas mõtlesid '{guessed_command}'?")
            continue

        try:
            result = parse_expression(expression, ans)
            ans = result
            formatted = format_number(result)
            print("Vastus:", formatted)
            history.append((expression, result))
        except ValueError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
