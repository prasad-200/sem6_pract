import random;

population=[5,10,15,20,25,30];

print("Initial population:",population);

binary_pop=[format(x,'05b')for x in population];

print("Binary popuation is :",binary_pop);

chromosome=random.choice(binary_pop);

print("The chromosome selected for mutation is:",chromosome);

ch_list=list(chromosome);

pos=random.randint(0,len(ch_list)-1);

if ch_list[pos] == '0':
    ch_list[pos] = '1';
else:
    ch_list[pos] = '0';

mutation=''.join(ch_list);

print("The bit chose for mutation is :",pos);

print("The child chromosome after mutation is ",mutation);

binary_pop[binary_pop.index(chromosome)]=mutation;

print("The population after mutation is:",binary_pop);

# Initial population: [5, 10, 15, 20, 25, 30]
# Binary popuation is : ['00101', '01010', '01111', '10100', '11001', '11110']
# The chromosome selected for mutation is: 01010
# The bit chose for mutation is : 0
# The child chromosome after mutation is  11010
# The population after mutation is: ['00101', '11010', '01111', '10100', '11001', '11110']