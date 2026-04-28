def lexical_analyzer(code):
    keywords = {"int", "float", "if", "else", "while", "return"}
    operators = {'+', '-', '*', '/', '='}

    tokens = code.split()

    for token in tokens:
        if token in keywords:
            print(f"{token} → Keyword")

        elif token.isdigit():
            print(f"{token} → Integer")

        elif token in operators:
            print(f"{token} → Operator")

        elif token.isidentifier():
            print(f"{token} → Identifier")

        else:
            print(f"{token} → Special Symbol")


# 🔹 Input
code = input("Enter code: ")

# 🔹 Output
print("\nTokens:")
lexical_analyzer(code)

int a = 10
Output:
int → Keyword
a → Identifier
= → Operator
10 → Integer