T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    field = [list(map(int, input().strip())) for _ in range(N)]

    start, end = N // 2, N // 2
    crops = 0
    for i in range(N):
        for j in range(start, end + 1):
            crops += field[i][j]

        if i < N // 2:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1
    print('#{} {}'.format(tc, crops))
