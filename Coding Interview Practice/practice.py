# Multiply two integers without the use of the '*' operator

def strange(a, b):
    answer = 0

    while(a != 0):
        answer += b
        a -= 1

    return answer

print(strange(3, 5))