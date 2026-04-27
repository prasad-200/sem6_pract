%{
#include<stdio.h>
%}

%%
[a-zA-Z]+ {printf("WORD\n");}
[0-9]+	{printf("NUMBER\n");}
.	{printf("OTHER");}
%%

int main(){
yylex();
return 0;
}

int yywrap(){

return 1;
}

output:

234
NUMBER

dfgg
WORD

prasad
WORD

prasad@1233
WORD
OTHERNUMBER

