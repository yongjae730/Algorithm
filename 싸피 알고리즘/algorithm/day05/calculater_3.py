def middle(arr):
    stack = []
    result = ''

    for ch in arr:

        if ch.isnumeric():   # 숫자라면 stack에 담는다.
            result += ch
        elif ch == '(':
            stack.append(ch)
        elif ch in ['*','/']:
            if len(stack)>0 and stack[-1] in ['*','/']:
                result += stack.pop()
            stack.append(ch)
        elif ch in ['-','+']:
            if len(stack)>0 and stack[-1] in ['*','/','-','+']:
                result += stack.pop()
            stack.append(ch)
        elif ch == ')':
            while len(stack) > 0 and stack[-1] != '(':
                result += stack.pop()
            stack.pop()

    while len(stack) > 0:
        result += stack.pop()


    return result

def Forth(cal):
    stack2 = []

    result = list(middle(cal).strip())

    for i in result:

        if i.isnumeric():
            stack2.append(int(i))

        elif i in '/*+-':
            if len(stack2) >= 2:
                if i == '+':
                    stack2[-2] = stack2[-2] + stack2[-1]
                elif i == '*':
                    stack2[-2] = stack2[-2] * stack2[-1]
                stack2.pop()
            else:
                return 'error'

    if len(stack2) == 1:
        return stack2[0]
    else:
        return 'error'

T = 10

for tc in range(1, 11):
    N = int(input())
    arr = input()

    print(middle(arr))
    print(Forth(arr))