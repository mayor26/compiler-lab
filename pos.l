%{
#include <stdio.h>

int word_count=0, noun_count=0, verb_count=0, adj_count=0;
int adv_count=0, pronoun_count=0, prep_count=0, det_count=0;
int num_count=0, punct_count=0;
%}

%option noyywrap

DELIM   [ \t\n]+
WORD    [A-Za-z]+
NUMBER  [0-9]+
PUNCT   [.,!?;:]

%%

the|a|an|this|that|these|those      { det_count++; word_count++; }
i|you|he|she|it|we|they|me|him|her|us|them   { pronoun_count++; word_count++; }
is|am|are|was|were|be|been|being|do|does|did|have|has|had   { verb_count++; word_count++; }
good|bad|big|small|new|old|young|quick|lazy|happy|sad|bright|dark { adj_count++; word_count++; }
quickly|slowly|very|too|also|well|here|there|now        { adv_count++; word_count++; }
in|on|at|by|with|for|to|from|of    { prep_count++; word_count++; }

{NUMBER}       { num_count++; word_count++; }
{PUNCT}        { punct_count++; }
{WORD}         { noun_count++; word_count++; }
{DELIM}        { /* ignore */ }

%%

int main() {
    printf("Enter a sentence:\n");
    yylex();

    printf("\n--- Parts of Speech Count ---\n");
    printf("Total Words: %d\n", word_count);
    printf("Nouns: %d\n", noun_count);
    printf("Verbs: %d\n", verb_count);
    printf("Adjectives: %d\n", adj_count);
    printf("Adverbs: %d\n", adv_count);
    printf("Pronouns: %d\n", pronoun_count);
    printf("Prepositions: %d\n", prep_count);
    printf("Determiners: %d\n", det_count);
    printf("Numbers: %d\n", num_count);
    printf("Punctuation: %d\n", punct_count);

    return 0;
}

%%
sudo apt update
sudo apt install flex gcc -y
Press : Ctr+x --> y --> enter (inside nano to save and come out of nano )

Step 3: Generate C Code from LEX
>>flex pos_lexer.l
this creates : lex,yy.c 

Step 4 :Compile the Program
>>gcc lex.yy.c -lfl -o pos_lexer

Step 5 : Run the Program
>>./pos_lexer

Step 6 :Give Input
The quick brown fox jumps over 2 lazy dogs.

Then Press:  Ctrl + D
