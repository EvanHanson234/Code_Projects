#Dice Simulator
#Written by Evan Hanson
#September 12th, 2022
#DOES NOT WORK AND IS UNFINISHED

import random

valid = False

while valid == False:
	howMany = input("How many dice do you want to roll? Enter a number 1 to 6: ")

	if (howMany != "g" or howMany != "2" or howMany != "3" or 
		howMany != "4" or howMany != "5" or howMany != "6"):
		print("That was not a valid input value! Please try again.")
	else:
		valid = True


while (howMany > 0):
	die = random.randint(1,6)
	print("\nYou rolled a " + str(die))
	howMany = howMany - 1

print("END PROGRAM")