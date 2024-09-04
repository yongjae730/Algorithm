T = int(input())

for tc in range(1, T + 1):
    laser = list(map(str, input().strip()))
    stack = []
    cnt = 0
    for i in range(len(laser)):
        if laser[i] == '(':
            stack.append(i)
        elif laser[i]== ')':
            if laser[i-1] == '(':
                stack.pop()
                cnt += len(stack)
            elif laser[i-1] == ')':
                stack.pop()
                cnt += 1
    print(f'#{tc} {cnt}')