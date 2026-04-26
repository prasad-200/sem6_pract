import random;

population=[5,10,15,20,25,30];

print("Initial population:",population);

binary_pop=[format(x,'05b') for x in population];

print("Initial Binary population:",binary_pop);

p1,p2=random.sample(binary_pop,2);

print("Selected parents are:");
print("Parent 1:",p1);
print("Parent 2:",p2);

point =len(p1)//2;

print("POINT is:",point);

c1=p1[:point]+p2[point:];
c2=p2[:point]+p1[point:];

print("Children 1 is:",c1);
print("Children 2 is:",c2);

binary_pop.remove(p1);
binary_pop.remove(p2);

binary_pop.append(c1);
binary_pop.append(c2);

print("Final population after crossover:",binary_pop);



# Initial population: [5, 10, 15, 20, 25, 30]
# Initial Binary population: ['00101', '01010', '01111', '10100', '11001', '11110']
# Selected parents are:
# Parent 1: 01010
# Parent 2: 00101
# POINT is: 2
# Children 1 is: 01101
# Children 2 is: 00010
# Final population is : ['01111', '10100', '11001', '11110', '01101', '00010']