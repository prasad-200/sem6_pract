%facts


male(prasad).
male(madhukar).
male(tukaram).
male(laxman).
male(harshal).


female(shreyasi).
female(sangeeta).
female(rambha).
female(mangla).


%parents relationships


parent(madhukar,prasad).
parent(sangeeta,prasad).
parent(madhukar,shreyasi).
parent(sangeeta,shreyasi).


parent(tukaram,madhukar).
parent(rambha,madhukar).
parent(tukaram,laxman).
parent(rambha,laxman).


parent(laxman,harshal).
parent(mangla,harshal).


%spouse
spouse(tukaram,rambha).
spouse(rambha,tukaram).


spouse(madhukar,sangeeta).
spouse(sangeeta,madhukar).


spouse(mangla,laxman).
spouse(laxman,mangla).


%Rules


father(X,Y):-parent(X,Y),male(X).
mother(X,Y):-parent(X,Y),female(X).


sibling(X,Y):-parent(Z,X),parent(Z,Y),X\=Y.


grandparent(X,Y):-parent(X,Z),parent(Z,Y).


grandfather(X,Y):-grandparent(X,Y),male(X).


ancestor(X,Y):-parent(X,Y).


ancestor(X,Y):-parent(X,Z),ancestor(Z,Y).


