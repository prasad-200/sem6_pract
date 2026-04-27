%{
#include<stdio.h>
%}

%%
[aeiouAEIOU]   {printf("VOWEL\n");}
[a-zA-Z]       {printf("CONSONENT\n");}
. {printf("Other\n");}
%%

int main(){
yylex();
return 0;
}

int yywrap(){
return 0;
}


ouptut:
@
Other

e
VOWEL

w
CONSONENT

