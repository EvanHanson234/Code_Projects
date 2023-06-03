#Tik Tac Toe
#Written by Evan Hanson
#September 18th, 2022

import random

# Global Variables ---------------------------------------------------------------- #
done = False
playerTurn = True
TL = " "	#Top Left
TC = " "	#Top Center
TR = " "	#Top Right
ML = " "	#Middle Left
MC = " "	#Middle Center
MR = " "	#Middle Right
BL = " "	#Bottom Left
BC = " "	#Bottom Center
BR = " "	#Bottom Right

# Instructions
print("Directions:")
print("TL = Top Left")
print("TC = Top Center")
print("TR = Top Right")
print("ML = Middle Left")
print("MC = Middle Center")
print("MR = Middle Right")
print("BL = Bottom Left")
print("BC = Bottom Center")
print("BR = Bottom Right")
print()

# Who goes first?
coinFlip = random.randint(0,1)
coinFlip = 0
if (coinFlip == 0):
	print("You get to go first!")
else:
	print("The CPU goes first!")
	playerTurn = False

# Win
def win():
	# Board
	print("---------------")
	print("-[" + TL + "]-[" + TC + "]-[" + TR + "]-")
	print("-[" + ML + "]-[" + MC + "]-[" + MR + "]-")
	print("-[" + BL + "]-[" + BC + "]-[" + BR + "]-")
	print("---------------")
	print("Congradulations! You are the Winner!")

def test():
	if ((TL == "X" and TC == "X" and TR == "X") or
	(ML == "X" and MC == "X" and MR == "X") or
	(BL == "X" and BC == "X" and BR == "X") or
	(TL == "X" and MC == "X" and BR == "X") or
	(BL == "X" and MC == "X" and TR == "X") or
	(TL == "X" and ML == "X" and BL == "X") or
	(TC == "X" and MC == "X" and BC == "X") or
	(TR == "X" and MR == "X" and BR == "X")):
		return True

def error():
	if (TL == " " and CPU == 1):
		return False
	elif (TC == " " and CPU == 2):
		return False
	elif (TR == " " and CPU == 3):
		return False
	elif (ML == " " and CPU == 4):
		return False
	elif (MC == " " and CPU == 5):
		return False
	elif (MR == " " and CPU == 6):
		return False
	elif (BL == " " and CPU == 7):
		return False
	elif (BC == " " and CPU == 8):
		return False
	elif (BR == " " and CPU == 9):
		return False
	else:
		CPUTurn = False
		return True
	
# Gameplay ------------------------------------------------------------------------ #
# Game Loop
while (done == False):
	
	if (playerTurn == True):
		# Board
		print("---------------")
		print("-[" + TL + "]-[" + TC + "]-[" + TR + "]-")
		print("-[" + ML + "]-[" + MC + "]-[" + MR + "]-")
		print("-[" + BL + "]-[" + BC + "]-[" + BR + "]-")
		print("---------------")

		# Player Play
		play = input("It is your turn.")
		if (TL == " " and play == "TL"):
			TL = "X"
		elif (TC == " " and play == "TC"):
			TC = "X"
		elif (TR == " " and play == "TR"):
			TR = "X"
		elif (ML == " " and play == "ML"):
			ML = "X"
		elif (MC == " " and play == "MC"):
			MC = "X"
		elif (MR == " " and play == "MR"):
			MR = "X"
		elif (BL == " " and play == "BL"):
			BL = "X"
		elif (BC == " " and play == "BC"):
			BC = "X"
		elif (BR == " " and play == "BR"):
			BR = "X"
		else:
			print("That is not a valid input. Please try again.")

		# Win?
		if (test()):
				done = True
				win()

		# CPU Play
		CPUTurn = True
		while ( CPUTurn == True ):
			CPU = random.randint(1,9)
			if ( not(error) ):
				if (TL == " " and CPU == 1):
					TL = "O"
					CPUTurn = False
				elif (TC == " " and CPU == 2):
					TC = "O"
					CPUTurn = False
				elif (TR == " " and CPU == 3):
					TR = "O"
					CPUTurn = False
				elif (ML == " " and CPU == 4):
					ML = "O"
					CPUTurn = False
				elif (MC == " " and CPU == 5):
					MC = "O"
					CPUTurn = False
				elif (MR == " " and CPU == 6):
					MR = "O"
					CPUTurn = False
				elif (BL == " " and CPU == 7):
					BL = "O"
					CPUTurn = False
				elif (BC == " " and CPU == 8):
					BC = "O"
					CPUTurn = False
				elif (BR == " " and CPU == 9):
					BR = "O"
					CPUTurn = False
		



