def lexical_analyzer(code):
    keywords = {"int", "float", "if", "else", "while", "return"}
    operators = {'+', '-', '*', '/', '=', '==', '!=', '<', '>', '<=', '>='}
    separators = {';', ',', '(', ')', '{', '}'}

    tokens = []
    temp = ""

    i = 0
    while i < len(code):
        ch = code[i]

        # Skip spaces
        if ch.isspace():
            if temp:
                tokens.append(temp)
                temp = ""
            i += 1
            continue

        # Check multi-character operators (==, !=, <=, >=)
        if i + 1 < len(code) and code[i:i+2] in operators:
            if temp:
                tokens.append(temp)
                temp = ""
            tokens.append(code[i:i+2])
            i += 2
            continue

        # Single char operators or separators
        if ch in operators or ch in separators:
            if temp:
                tokens.append(temp)
                temp = ""
            tokens.append(ch)
            i += 1
            continue

        # Build identifiers / numbers
        temp += ch
        i += 1

    if temp:
        tokens.append(temp)

    # Classification
    for token in tokens:
        if token in keywords:
            print(f"{token} → Keyword")

        elif token.isdigit():
            print(f"{token} → Constant")

        elif token in operators:
            print(f"{token} → Operator")

        elif token in separators:
            print(f"{token} → Separator")

        elif token.isidentifier():
            print(f"{token} → Identifier")

        else:
            print(f"{token} → Unknown")


# 🔹 Input
code = input("Enter code: ")

print("\nTokens:")
lexical_analyzer(code)