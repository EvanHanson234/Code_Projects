# Multiply two integers without the use of the '*' operator

def strangeMultiply(a, b):
    answer = 0

    while (a != 0):
        answer += b
        a -= 1

    print(answer)

strangeMultiply(7, 10)