T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    balloons = [list(map(int, input().split())) for _ in range(N)]

    di = [1, 0, 0, -1]
    dj = [0, 1, -1, 0]

    max_total = 0

    for i in range(N):
        for j in range(M):
            total = balloons[i][j]
            for k in range(4):
                ci, cj = i + di[k], j + dj[k]
                if 0 <= ci < N and 0 <= cj < M:
                    total += balloons[ci][cj]

            if max_total < total:
                max_total = total
    print(f'#{tc} {max_total}')