# Given a string, reverse the order of the words in the string, 
# without reversing the characters in the words. input: "The cat ran away." Output: "away. ran cat The"



def reverse1(a):
    answer = ""
    words = a.split()

    for i in range(len(words)-1, -1, -1):
        answer += words[i] + " "

    print(answer.strip())

reverse1("The cat ran away. and then it ran away again.")

def reverse_words(s):
    words = s.split()
    reversed_words = reversed(words)
    reversed_s = ' '.join(reversed_words)
    return reversed_s

input_string = "The cat ran away."
reversed_string = reverse_words(input_string)
print(reversed_string)