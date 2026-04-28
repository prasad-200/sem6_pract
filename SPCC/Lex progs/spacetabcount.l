%{
#include<stdio.h>
int space=0;
int tab=0;
%}

%%
[" "]  {space++;}
["\t]	{tab++;}
.	{}
%%

int main(){
yylex();
printf("\nSpace count:%d \n Tab count:%d \n ",space,tab);
return 0;
}

int yywrap(){
return 1;
}

I am Prasad  

TSEC    NOT	GOATED


Space count:2 
 Tab count:2 

