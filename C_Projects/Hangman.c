/*	Hangman
	Written by Evan Hanson
	September 9th, 2022		*/

#include "stdio.h"
#include "stdlib.h"
#include "string.h"

int main() {

	printf("hello world");

	char guessWords[][16] = {
		"green",
		"yellow",
		"windows",
		"linux",
		"apple"
	};

	int randomIndex = rand() % 6;
	int loopIndex = 0;
	int fullrand = 0;
	for(loopIndex = 0; loopIndex < 5; loopIndex++) {
		fullrand = rand();
		randomIndex = fullrand % 6;
		printf("%d -> %d\n" ,fullrand, randomIndex);
	}

	return 0;
}