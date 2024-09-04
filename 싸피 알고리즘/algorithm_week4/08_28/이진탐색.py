def inorder(node):
    global number
    if node > N:
        return

    inorder(node * 2)
    number += 1
    num[node] = number
    inorder(node * 2 + 1)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    number = 0
    num = [0] * (N + 1)

    inorder(1)

    print('#{} {} {}'.format(tc, num[1], num[N // 2]))
