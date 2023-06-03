# Decrypt The Message
# Evan Hanson
# 06/03/2023
# You will need to have the key.txt file in the same directory as this file.


import string


chars = " " + string.ascii_letters + string.digits + string.punctuation  # Creates a string of all the characters
chars = list(chars)         # Converts the string of characters into a list of characters

# Read the key from the file
with open("key.txt", "r") as file:
    key = list(file.read().strip())

cipher_text = input("Enter the encrypted message: ")        # Gets the encrypted message
plain_text = ""                                             # Creates an empty string to store the decrypted message


# Decryption
for letter in cipher_text:                   # Iterates through each letter in the message
    index = key.index(letter)                # Gets the index of the letter in the list of characters
    plain_text += chars[index]               # Adds the character at the same index in the shuffled list of characters to the decrypted message

print(f"\nEncrypted message: {cipher_text}") # Prints the encrypted message
print(f"Decrypted message: {plain_text}")    # Prints the decrypted message
print("\n")
