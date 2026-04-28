%{
#include<stdio.h>
%}

%%
[_a-zA-Z][0-9_a-zA-Z]*	{printf("Valid identifier:%s",yytext);}
[0-9]+			{printf("INvalid identifier:%s",yytext);}
.	{};
%%

int main(){
yylex();
return 0;
}

int yywrap(){
return 1;
}

count
Valid identifier:count
1count
INvalid identifier:1Valid identifier:count

