T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]

    mx_len = 0
    for x in range(N):
        for y in range(M):
            if arr[x][y] == 1:
                for k in range(4):
                    stack = []
                    stack.append(1)
                    cx, cy = x + dx[k], y + dy[k]
                    while 0 <= cx < N and 0 <= cy < M and arr[cx][cy] == 1:
                        stack.append(1)
                        cx, cy = cx + dx[k], cy + dy[k]
                    if len(stack) > mx_len:
                        mx_len = len(stack)
    if mx_len == 1:
        mx_len = 0

    print(f'#{tc} {mx_len}')
