for tc in range(1,11):
    N, password = map(str, input().split())
    n = int(N)

    stack = []

    for i in range(n):

        if len(stack) == 0:
            stack.append(password[i])

        elif password[i] != stack[-1]:
            stack.append((password[i]))

        elif password[i] == stack[-1]:
            stack.pop()

    if 0 == stack[0]:
        stack.remove(0)

    print(f'#{tc} ', *stack, sep='')
