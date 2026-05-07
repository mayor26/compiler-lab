%{
#include <stdio.h>
#include <stdlib.h>

void yyerror(char *s);
int yylex();
%}

%token NUMBER

/* Operator precedence (VERY IMPORTANT) */
%left '+' '-'
%left '*' '/'

%%

input:
    | input line
    ;

line:
      '\n'
    | exp '\n'  { printf("Result = %d\n", $1); }
    ;

exp:
      NUMBER        { $$ = $1; }
    | exp '+' exp   { $$ = $1 + $3; }
    | exp '-' exp   { $$ = $1 - $3; }
    | exp '*' exp   { $$ = $1 * $3; }
    | exp '/' exp   { $$ = $1 / $3; }
    | '(' exp ')'   { $$ = $2; }
    ;

%%

void yyerror(char *s) {
    printf("Error: %s\n", s);
}

int main() {
    printf("Enter expression:\n");
    yyparse();
    return 0;
}

calc.y
---------------------
%{
#include "y.tab.h"
#include <stdlib.h>
%}

%%

[0-9]+      { yylval = atoi(yytext); return NUMBER; }
[ \t]       ;   /* ignore spaces/tabs */
\n          return '\n';   /* IMPORTANT: send newline to YACC */
.           return yytext[0];   /* return operators like + - * / ( ) */

%%

int yywrap() {
    return 1;
}

calc.l

Install tools (once)
sudo apt update
sudo apt install flex bison gcc -y

 Clean old builds (IMPORTANT)
rm -f lex.yy.c y.tab.c y.tab.h calc

 Generate parser (YACC)
yacc -d calc.y

 Creates:
    • y.tab.c → parser code 
    • y.tab.h → token definitions 

 Generate scanner (LEX)
lex calc.l
Creates:  lex.yy.c → lexical analyzer 

 Compile : gcc lex.yy.c y.tab.c -o calc -lfl

 Run: ./calc


