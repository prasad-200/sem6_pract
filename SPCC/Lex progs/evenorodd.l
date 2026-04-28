%{
#include<stdio.h>

%}


%%
[0-9]*[02468] {printf("Even no:%s",yytext);}
[0-9]*[13579] {printf("Odd no : %s",yytext);}
.	{}

%%


int main(){
yylex();
return 0;
}

int yywrap(){
return 1;
}

122    
Even no:122
121
Odd no : 121
0
Even no:0
1
Odd no : 1



