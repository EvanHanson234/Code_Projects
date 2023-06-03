# Encrypt The Message
# Evan Hanson
# 06/03/2023

import random
import string


chars = " " + string.ascii_letters + string.digits + string.punctuation  # Creates a string of all the characters
chars = list(chars)         # Converts the string of characters into a list of characters
key = chars.copy()          # Creates a copy of the list of characters

random.shuffle(key)         # Shuffles the list of characters 

#print(f"chars: {chars}")    # Prints the list of characters
#print(f"key: {key}")        # Prints the shuffled list of characters

# Save the key to a file
with open("key.txt", "w") as file:
    file.write("".join(key))
    

# Encryption
plain_text = input("Enter a message: ")    # Gets the message to encrypt
cipher_text = ""                           # Creates an empty string to store the encrypted message

for letter in plain_text:                  # Iterates through each letter in the message
    index = chars.index(letter)            # Gets the index of the letter in the list of characters
    cipher_text += key[index]              # Adds the character at the same index in the shuffled list of characters to the encrypted message

print(f"\nPlain message: {plain_text}") # Prints the plain message
print(f"Encrypted message: {cipher_text}") # Prints the encrypted message
print("\n")
