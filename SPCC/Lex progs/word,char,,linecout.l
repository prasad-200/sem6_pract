%{

#include<stdio.h>
int line=0,charc=0,word=0;
%}

%%

\n {line++;charc++;}
[ \t]	{charc+=yyleng;}
[^ \n\t]+	{charc+=yyleng;word++;}

%%

int main(){
yylex();
printf("WORDs:%d\nlines:%d\nchars:%d\n",word,line,charc);
return 0;
}

int yywrap(){
return 1;
}
