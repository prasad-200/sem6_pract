def remove_leftfact(production):
    new_production={};

    for non_terminal in production:
        prods=production[non_terminal];

        if len(prods)<2:
            new_production[non_terminal]=prods;

        prefix=prods[0];
        for prod in prods[1:]:
            i=0;
            while i<len(prefix) and len(prod) and prefix[i]==prod[i]:
                i+=1;
            prefix=prod[:i];
            
            if prefix:
                nt=non_terminal+"'";
                new_production[non_terminal]=[prefix+nt];
                new_production[nt]=[];
                for prod in prods:
                    suffix=prod[len(prefix):];
                    if suffix=="":
                        suffix='e';
                    new_production[nt].append(suffix)
            else:
                new_production[non_terminal]=prods

    return new_production;




n=int(input("Enter the number of productions: "));
production={};

for i in range(n):
    lhs=input("Enter the lhs of production rule :");
    rhs=input(f"Enter the rhs rules of {lhs}(use'|'):").split('|');
    production[lhs]=rhs;

result=remove_leftfact(production);

print("\n Grammert after removing left recursion:");
for nt in result:
    print(f"{nt}->{'|'.join(result[nt])}");
