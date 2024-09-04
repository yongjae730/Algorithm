def start(arr, N):
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 2:
                return x, y


def maze(arr, N):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    cx, cy = start(arr, N)
    stack = []
    stack.append([cx, cy])

    while stack:
        cx, cy = stack.pop()

        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]

            while 0 <= nx < N and 0 <= ny < N and (arr[nx][ny] == 0 or arr[nx][ny] == 3) and visited[nx][ny] == 0:
                stack.append([nx, ny])
                visited[nx][ny] = 1
                if arr[nx][ny] == 3:
                    return 1

    return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]

    print(f'#{tc} {maze(arr, N)}')
