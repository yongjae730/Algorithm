def min_sum(x, y, sum_num):
    global result
    if x == N - 1 and y == N - 1:
        sum_num += arr[x][y]
        if result > sum_num:
            result = sum_num
            return
    if result < sum_num:
        return
    dx = [0, 1]
    dy = [1, 0]

    for k in range(2):
        ni, nj = x + dx[k], y + dy[k]
        if x > N - 1 or y > N - 1:
            continue
        if not visited[x][y]:
            visited[x][y] = 1
            min_sum(ni, nj, sum_num + arr[x][y])
            visited[x][y] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)]for _ in range(N)]
    result = 999
    min_sum(0, 0, 0)

    print(f'#{tc} {result}')
