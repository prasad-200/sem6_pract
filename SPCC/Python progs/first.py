def first(production,first_set,symbol):
    if not symbol.isupper():
        return {symbol};
    if symbol in first_set:
        return first_set[symbol];

    
    result_set=set();
    for prods in production[symbol]:

        if prods=='e':
            result_set.add('e');
            continue
        for char in prods:
            result=first(production,first_set,char);
            result_set.update(result-{'e'});
            if 'e' not in result:
                break;
        else:
            result_set.add('e');
    first_set[symbol]=result_set;
    return result_set;

n=int(input("Enter the number of productions: "));
production={};

for i in range(n):
    lhs=input("Enter the lhs of production rule :");
    rhs=input(f"Enter the rhs rules of {lhs}(use'|'):").split('|');
    production[lhs]=rhs;

print("FIRST sets of all non terminals :")
first_set={};
for non_terminal in production:
    result=first(production,first_set,non_terminal);
    print(f"First of {non_terminal}:{{ {','.join(result)} }}");


# Enter the number of productions: 3
# Enter the lhs of production rule :E
# Enter the rhs rules of E(use'|'):T|R
# Enter the lhs of production rule :T
# Enter the rhs rules of T(use'|'):a|e
# Enter the lhs of production rule :R
# Enter the rhs rules of R(use'|'):b|e
# FIRST sets of all non terminals :
# First of E:{ e,b,a }
# First of T:{ e,a }
# First of R:{ b,e }