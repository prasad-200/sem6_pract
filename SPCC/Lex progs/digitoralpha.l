%{
#include<stdio.h>
%}

%%

[0-9]  {printf("\nDIGIT");}
[a-zA-Z]   {printf("\nAlphabet");}
.          {printf("\n other");}

%%

int main(){
yylex();
return 0;
}

int yywrap(){
return 1;
}

output:
0
DIGIT
4

DIGIT
a

Alphabet

!

 other

