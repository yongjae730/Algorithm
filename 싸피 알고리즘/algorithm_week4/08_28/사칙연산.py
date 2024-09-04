def check(node):
    global result

    # if node == 0:
    #     return
    if calculator[node] not in ['*', '+', '/', '-']:
        return int(calculator[node])

    A = check(left[node])
    B = check(right[node])




    if calculator[node] == '*':
        return A * B
    elif calculator[node] == '+':
        return A + B
    elif calculator[node] == '-':
        return A - B
    elif calculator[node] == '/':
        return A // B


T = 10

for tc in range(1, T + 1):
    N = int(input())

    calculator = ['0'] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    result = 0
    for _ in range(N):
        data = input().split()
        if len(data) == 4:
            node, cal, l_child, r_child = data
            calculator[int(node)] = cal
            left[int(node)] = int(l_child)
            right[int(node)] = int(r_child)
        elif len(data) == 2:
            node, cal = data
            calculator[int(node)] = cal

    print(f'#{tc} {check(1)}')
