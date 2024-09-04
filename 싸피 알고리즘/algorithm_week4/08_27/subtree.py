T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    parents = [0] * (E + 2)
    left = [0] * (E + 2)
    right = [0] * (E + 2)
    cnt = 0

    for i in range(0, len(arr), 2):
        parent, child = arr[i], arr[i + 1]

        if left[parent] == 0:
            left[parent] = child
        else:
            right[parent] = child

        parents[child] = parent

    stack = []
    stack.append(N)
    while stack:
        cnt += 1
        N = stack.pop()
        if left[N] != 0:
            stack.append(left[N])
        if right[N] != 0:
            stack.append(right[N])

    print(f'#{tc} {cnt}')
