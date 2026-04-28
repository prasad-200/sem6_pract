%{
#include<stdio.h>

%}


%%
"int"|"float"|"char"|"if"|"else"|"for"|"while"|"return"	{printf("Keywords:%s",yytext);}
[0-9]+"."[0-9]+	{printf("Float:%s\n",yytext);}
[0-9]+		{printf("Intger:%s\n",yytext);}
[a-zA-Z_][a-zA-Z_0-9]*	{printf("Identifier:%s\n",yytext);}
[+\-/*=]	{printf("OPerator:%s\n",yytext);}
[ \t\n]		{}
. 		{printf("Special character:%s\n",yytext);}
%%


int main(){
yylex();
return 0;
}

int yywrap(){
return 1;
}

int a=9+9.98
Keywords:intIdentifier:aOPerator:=Intger:9OPerator:+Float:9.98


