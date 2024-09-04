def Forth(arr):
    stack = []
    for i in arr:
        if i not in '+-*/.':
            stack.append(int(i))

        elif i in '+-*/':
            if len(stack) >= 2:
                if i == '+':
                    stack[-2] = stack[-2] + stack[-1]
                elif i == '-':
                    stack[-2] = stack[-2] - stack[-1]
                elif i == '*':
                    stack[-2] = stack[-2] * stack[-1]
                elif i == '/':
                    if stack[-1]:
                        stack[-2] = stack[-2] // stack[-1]
                    else:
                        return 'error'
                stack.pop()
            else:
                return 'error'
        elif i == '.':
            if len(stack) == 1:
                return stack[0]
            else:
                return 'error'


T = int(input())

for tc in range(1, T + 1):
    arr = list(input().split())

    print(f'#{tc} {Forth(arr)}')
