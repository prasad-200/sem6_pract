%{
#include<stdio.h>
#include<string.h>
char str[100];
%}


%%
[a-zA-Z]+	{
	strcpy(str,yytext);
	int i=0,j=strlen(str)-1,flag=1;
	while (i<j){
		if(str[i]!=str[j]){
			flag=0;
			break;
			}
			i++;
			j--;
	}
	if(flag){
	 printf("palindrome is : %s",str);
	 }
	 else{
	 printf("NOt palindrome : %s",str);
	 }

}
[" \t\n"] {}
.	{}

%%


int main(){
yylex();
return 0;
}

int yywrap(){
return 1;
}

maam
palindrome is : maam
madam
palindrome is : madam
prasad
NOt palindrome : prasad

