import random

# Fitness function
def fitness(ch):
    a, b, c, d = map(int, ch)
    return (a + 2*b + 3*c + 4*d) - 30


# Step 1: Initial population
population = ['1010', '1111', '0001', '0101', '1001', '0110']

print("Initial Population:", population)

# Step 2: Fitness
fit = [fitness(ch) for ch in population]

print("\nFitness Values:")
for i in range(len(population)):
    print(population[i], ":", fit[i])

# Step 3: Selection (top 2)
selected = sorted(zip(population, fit), key=lambda x: x[1], reverse=True)[:2]

p1 = selected[0][0]
p2 = selected[1][0]

print("\nSelected Parents:", p1, p2)

# Step 4: Crossover
point = 2
c1 = p1[:point] + p2[point:]
c2 = p2[:point] + p1[point:]

print("\nAfter Crossover:", c1, c2)

# Step 5: Mutation (flip 1 bit in c1)
c1_list = list(c1)
pos = random.randint(0, 3)

c1_list[pos] = '1' if c1_list[pos] == '0' else '0'
c1 = ''.join(c1_list)

print("\nAfter Mutation:", c1)

# Step 6: Replace worst 2
population = sorted(zip(population, fit), key=lambda x: x[1])
population = [p[0] for p in population]

population[0] = c1
population[1] = c2

print("\nFinal Population:", population)

# Step 7: Best chromosome
final_fit = [fitness(ch) for ch in population]

best_index = final_fit.index(max(final_fit))

print("\nBest Chromosome:", population[best_index])
print("Fitness:", final_fit[best_index])
🔹 🧠 Important understanding

👉 Values will be negative (because -30)
✔ So:

-20 is better than -25
🔹 🧾 Sample Output (idea)
Initial Population: ['1010', '1111', '0001', '0101', '1001', '0110']

Fitness:
1010 : -25
1111 : -20
...

Selected Parents: 1111 1010

After Crossover: 1110 1011

After Mutation: 1100

Final Population: ['1100', '1011', '1001', '0110', '0101', '1111']

Best Chromosome: 1111
Fitness: -20