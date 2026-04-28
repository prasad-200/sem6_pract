%{
#include<stdio.h>
int operands=0;int operator=0;
%}


%%
[+\-*/=]	{operator++;}
[a-zA-Z0-9]+	{operands++;}
[ \n\t]		{}
.		{}
%%


int main(){
yylex();
printf("operator are :%d\n operands are:%d\n",operator,operands);
return 0;
}

int yywrap(){
return 1;
}

a=b+c
operator are :2
 operands are:3

