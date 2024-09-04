T = int(input())

for tc in range(1,T+1):
    S = input()
    stack = []
    cnt = 0
    for i in S:
        if i =='(':
            stack.append(i)

        elif i == ')':
            if '(' in stack or '|' in stack:
                cnt += 1
                stack = []

        elif i == '|':
            if '(' in stack:
                cnt += 1
                stack = []
            else:
                stack.append(i)
        else:
            continue
    print(f'#{tc} {cnt}')