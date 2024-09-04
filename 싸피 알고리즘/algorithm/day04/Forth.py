T = int(input())

for tc in range(1, T + 1):
    forth = input()
    stack = []

    for ch in forth:
        if len(stack) > 1:
            A = stack[-1]
            B = stack[-2]

            if forth.isnumeric():
                stack.append(ch)

            elif ch in ['*', '/']:
                stack[-1]
