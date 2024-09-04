T = int(input())
for _ in range(T):
    word = input()
    stack = []
    flag = True
    for i in word:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) > 0:
                stack.pop(-1)
            else:
                flag = False
    if len(stack) == 0 and flag == True:
        print('YES')
    else:
        print('NO')
