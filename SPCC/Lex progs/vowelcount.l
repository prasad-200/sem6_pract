%{
#include<stdio.h>
int count=0;
%}


%%

[aeiouAEIOU]	{count=count+1;}
.		{} 

%%

int main(){
yylex();
printf("NUmber of vowels are :%d\n",count);
return 0;
}

int yywrap(){
return 1;

}

AEIOUpppp    

NUmber of vowels are :5

