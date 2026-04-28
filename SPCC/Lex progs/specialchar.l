%{
#include<stdio.h>
%}

%%
[0-9a-zA-Z] {}
[ \n\t]	{}
.		{printf("Special character is %s\n",yytext);}

%%

int main(){
yylex();
return 0;
}

int yywrap(){
return 1;
}

i am prasad@123}!
Special character is @Special character is }Special character is !

