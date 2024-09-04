T = int(input())

for tc in range(1, T+1):
    ground = input()
    cnt = 0
    stack = []
    for i in ground:

        if i == '(':
            stack.append(i)
        elif i == '|':
            if '(' in stack:
                cnt += 1
                stack = []
            else:
                stack.append(i)
        elif i == ')':
            if '(' in stack or '|' in stack:
                cnt += 1
                stack = []
        else:
            stack = []
    print('#{} {}'.format(tc,cnt))

