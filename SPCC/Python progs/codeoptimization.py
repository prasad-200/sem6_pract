print("Name: Prasad Patil C24 2303127")
print("Experiment 6 - Code Optimization\n")


n = int(input("Enter number of statements: "))


expr_seen = set()
optimized = []


for i in range(n):
    stmt = input("Enter statement: ")
    left, right = stmt.split("=")


    if right not in expr_seen:
        expr_seen.add(right)
        optimized.append(f"{left} = {right}")


print("\nOptimized Code:")


count = 1
for line in optimized:
    left, right = line.split("=")
    print(f"t{count} ={right}")
    count += 1