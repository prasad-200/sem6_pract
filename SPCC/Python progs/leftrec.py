def remove_leftrec(productions):
    new_production={};

    for non_terminal in productions:
        alpha=[];
        beta=[];

        for prod in productions[non_terminal]:
            if prod.startswith(non_terminal):
                alpha.append(prod[len(non_terminal):]);
            else:
                beta.append(prod);

        if alpha:
            new_nt=non_terminal+"'";
            new_production[non_terminal]=[b+new_nt for b in beta];
            new_production[new_nt]=[a+new_nt for a in alpha]+['E'];
        else:
            new_production[non_terminal]=productions[non_terminal];

    return new_production;
        



n=int(input("Enter the number of productions: "));
production={};

for i in range(n):
    lhs=input("Enter the lhs of production rule :");
    rhs=input(f"Enter the rhs rules of {lhs}(use'|'):").split('|');
    production[lhs]=rhs;

result=remove_leftrec(production);

print("\n Grammert after removing left recursion:");
for nt in result:
    print(f"{nt}->{'|'.join(result[nt])}");

# Enter the number of productions: 1
# Enter the lhs of production rule :A
# Enter the rhs rules of A(use'|'):Aa|b

#  Grammert after removing left recursion:
# A->bA'
# A'->aA'|E