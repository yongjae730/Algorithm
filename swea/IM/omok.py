def omok(arr, N):
    dx = [0, 1, 1, 1]
    dy = [1, 1, 0, -1]
    for x in range(N):
        for y in range(N):
            for k in range(4):
                stack = []
                if arr[x][y] == 'o':
                    stack.append(arr[x][y])
                    cx, cy = x + dx[k], y + dy[k]
                    while 0 <= cx < N and 0 <= cy < N and arr[cx][cy] == 'o':
                        stack.append(arr[cx][cy])
                        cx, cy = cx + dx[k], cy + dy[k]
                    if len(stack) == 5:
                        return 'YES'

    return "NO"


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input().strip()) for _ in range(N)]

    result = omok(arr, N)

    print(f'#{tc} {result}')
