import sys

while True:
    arr = sys.stdin.readline()
    stack = []
    if arr[0] == '.':
        break
    flag = True
    for i in range(len(arr)):

        if arr[i] in ['(', '[']:
            stack.append(arr[i])
        elif arr[i] == ')':
            if len(stack)>0 and stack[-1] == '(':
                stack.pop()
            else:
                flag = False
        elif arr[i] == ']':
            if len(stack)>0 and stack[-1] == '[':
                stack.pop()
            else:
                flag = False
    if len(stack) or flag == False:
        print('no')
    else:
        print('yes')
