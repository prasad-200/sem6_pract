def follow(production, first_sets, start_symbol):
    follow_sets = {nt: set() for nt in production}
    follow_sets[start_symbol].add('$')

    changed = True

    while changed:
        changed = False

        for lhs in production:
            for prod in production[lhs]:
                for i in range(len(prod)):
                    B = prod[i]

                    if B.isupper():
                        # Case: A → αBβ
                        if i + 1 < len(prod):
                            beta = prod[i + 1]

                            before = len(follow_sets[B])

                            # FIRST(beta)
                            first_beta = first_sets.get(beta, {beta})

                            follow_sets[B].update(first_beta - {'e'})

                            if 'e' in first_beta:
                                follow_sets[B].update(follow_sets[lhs])

                            if len(follow_sets[B]) > before:
                                changed = True

                        # Case: A → αB
                        else:
                            before = len(follow_sets[B])

                            follow_sets[B].update(follow_sets[lhs])

                            if len(follow_sets[B]) > before:
                                changed = True

    return follow_sets


# 🔹 INPUT
n = int(input("Enter number of productions: "))
production = {}

for _ in range(n):
    lhs = input("Enter LHS: ")
    rhs = input(f"Enter RHS for {lhs} (use |): ").split('|')
    production[lhs] = rhs

# 🔹 FIRST input (given)
first_sets = {}
m = int(input("\nEnter number of FIRST sets: "))

for _ in range(m):
    nt = input("Enter non-terminal: ")
    vals = input(f"Enter FIRST({nt}) (comma separated): ").split(',')
    first_sets[nt] = set(vals)

start_symbol = list(production.keys())[0]

# 🔹 FOLLOW
follow_sets = follow(production, first_sets, start_symbol)

print("\nFOLLOW sets:")
for nt in follow_sets:
    print(f"FOLLOW({nt}) = {{ {', '.join(follow_sets[nt])} }}")

    Input
Enter number of productions: 3
E
TR
T
a|e
R
b|e

Enter number of FIRST sets: 3
E
a,b,e
T
a,e
R
b,e
🔹 Output
FOLLOW(E) = { $ }
FOLLOW(T) = { b, $ }
FOLLOW(R) = { $ }