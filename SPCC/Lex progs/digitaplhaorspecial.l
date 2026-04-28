%{
#include<stdio.h>

int special,digit,charac=0;

%}

%%
[0-9]+  {digit+=yyleng;}
[a-zA-Z]+	{charac+=yyleng;}
[ \n\t]		{}
.		{special++;}

%%

int main(){
yylex();
printf("\nDIGITS:%d\nCHARACTER:%d\nspecial:%d\n",digit,charac,special);
}

int yywrap(){
return 1;
}

I ma prasad 
my age is 21
@#$^

DIGITS:2
CHARACTER:16
special:4


