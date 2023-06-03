#Number Guessing
#Written by Evan Hanson
#September 9th, 2022

import random

#global variables
target = random.randint(1,100)
guess = 0
score = 100

#user loses
def lose():
	print("\nSorry! You did not guess the correct number!")
	print("Your Score: " + str(score))
	print("\n")

#user wins
def win():
	print("\nCongratulations! You guessd the correct number!")
	print("Your Score: " + str(score))
	print("\n")

#prints your initial score of 100
print("Your Score: " + str(score))

#user's first guess
guess = int(input("\nEnter a number guess! "))

#loop through as user tries to guess the correct number
while (guess != target):

	if (guess > target):
		print("\nThe target is smaller. Try again.")
		score = score - 10
		print("Your Score: " + str(score))

	else:
		print("\nThe target is larger. Try again.")
		score = score - 10
		print("Your Score: " + str(score))

	if (score <= 0):
		lose()
		break

	guess = int(input("\nEnter a new number. "))

if (guess == target):
	win()
