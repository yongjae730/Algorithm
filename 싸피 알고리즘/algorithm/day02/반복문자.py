T = int(input())

for tc in range(1,T+1):
    text = input()

    stack = []

    for i in range(len(text)):

        if len(stack) == 0:
            stack.append(text[i])

        elif text[i] != stack:
            stack.append((text[i]))

        elif text[i] == stack[-1]:
            stack.pop()

    print(f'#{tc} {len(stack)}')