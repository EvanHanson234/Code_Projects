# Given a string, reverse the order of the words in the string, 
# without reversing the characters in the words. input: "The cat ran away." Output: "away. ran cat The"

def reverseOrder(a):
    answer = ""
    words = a.split()
    words = reversed(words)
    answer = " ".join(words)
    print(answer)

reverseOrder("The cat ran away.")