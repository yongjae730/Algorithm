T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]
    max_total = 0
    for x in range(N):
        for y in range(M):
            total = arr[x][y]
            for k in range(4):
                for l in range(1, arr[x][y] + 1):
                    cx, cy = x + dx[k] * l, y + dy[k] * l
                    if 0 <= cx < N and 0 <= cy < M:
                        total += arr[cx][cy]

            if total > max_total:
                max_total = total

    print(f'#{tc} {max_total}')
