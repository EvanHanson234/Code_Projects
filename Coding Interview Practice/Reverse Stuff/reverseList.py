def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """
    stack = []
    reversed_list = []
    
    for item in s:
        stack.append(item)
        
    while(stack):
        reversed_list.append(stack.pop())
        
    print(reversed_list)

reverseString("blank")