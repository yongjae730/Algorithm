def preorder(node):
    global result
    if node == 0:
        return
    preorder(left[node])
    result += word[node]
    preorder(right[node])


T = 10
for tc in range(1, T + 1):
    N = int(input())
    result = ''
    left = [0] * (N + 1)
    right = [0] * (N + 1)
    word = ['0'] * (N + 1)
    for i in range(N):
        order = list(map(str, input().split()))
        if len(order) == 4:
            right[int(order[0])] = int(order[3])
        if len(order) >= 3:
            left[int(order[0])] = int(order[2])
            word[int(order[0])] = order[1]
        else:
            word[int(order[0])] = order[1]

    preorder(1)
    print(f'#{tc} {result}')
