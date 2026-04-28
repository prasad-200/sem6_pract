%{
#include<stdio.h>

%}


%%
[0-9]+"."[0-9]+	{printf("Floating point is: %s",yytext);}
[0-9]+  {printf("INterger is:%s",yytext);}
.	{}
%%


int main(){
yylex();
return 0;
}

int yywrap(){
return 1;
}

9
INterger is:9
9.87
Floating point is: 9.87

