T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    othello = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    # 기본 돌 깔기
    B = 1
    W = 2
    othello[N // 2][N // 2] = W
    othello[N // 2][N // 2 + 1] = B
    othello[N // 2 + 1][N // 2] = B
    othello[N // 2 + 1][N // 2 + 1] = W
    for i in range(M):
        X, Y, color = map(int, input().split())
        othello[X][Y] = color
        stack = []

        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]
        if othello[X][Y] == B:
            for k in range(8):
                cx, cy = X + dx[k], Y + dy[k]
                while 1 <= cx < N + 1 and 1 <= cy < N + 1 and othello[cx][cy] == W:
                    stack.append([cx, cy])
                    cx, cy = cx + dx[k], cy + dy[k]

                if 1 <= cx < N + 1 and 1 <= cy < N + 1 and othello[cx][cy] == B:
                    for i, j in stack:
                        othello[i][j] = B
                else:
                    stack = []

        if othello[X][Y] == W:
            for k in range(8):
                cx, cy = X + dx[k], Y + dy[k]
                while 1 <= cx < N + 1 and 1 <= cy < N + 1 and othello[cx][cy] == B:
                    stack.append([cx, cy])
                    cx, cy = cx + dx[k], cy + dy[k]

                if 1 <= cx < N + 1 and 1 <= cy < N + 1 and othello[cx][cy] == W:
                    for i, j in stack:
                        othello[i][j] = W
                else:
                    stack = []
    Black = 0
    White = 0
    for j in range(len(othello)):
        Black += othello[j].count(1)
        White += othello[j].count(2)

    print(f'#{tc} {Black} {White}')
