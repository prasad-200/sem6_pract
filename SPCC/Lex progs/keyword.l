%{
#include<stdio.h>

%}


%%
"int"|"float"|"char"|"if"|"else"|"for"|"while"|"return"    {printf("\nKeyword is :%s",yytext);}
[a-zA-Z_][0-9a-zA-Z_]*	{printf("\nIdentifer is : %s",yytext);}
[ \n\t] {}
.	{}
%%


int main(){
yylex();
return 0;
}

int yywrap(){
return 1;
}

int
Keyword is :int

float
Keyword is :float
count
Identifer is : count

