symbol_table = {}

sizes = {
    "int": 4,
    "float": 4,
    "char": 1,
    "double": 8
}

n = int(input("Enter number of lines of code: "))

for _ in range(n):
    line = input().strip()

    parts = line.replace(';', '').split()

    if len(parts) < 2:
        continue

    dtype = parts[0]

    if dtype in sizes:
        variables = "".join(parts[1:]).split(',')

        for var in variables:
            symbol_table[var] = (dtype, sizes[dtype])

print("\nSymbol Table:")
print("Name\tType\tSize")

for var in symbol_table:
    dtype, size = symbol_table[var]
    print(f"{var}\t{dtype}\t{size}")

 🔹 Input
Enter number of lines of code: 3
int a, b;
float x;
char c;
🔹 Output
Symbol Table:
Name    Type    Size
a       int     4
b       int     4
x       float   4
c       char    1