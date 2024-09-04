T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # N = 보드 한 변의 길이,  M = 돌을 놓는 횟수
    board = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    B = 1
    W = 2
    # 기본 돌 놓기
    board[N // 2][N // 2] = 2
    board[N // 2 + 1][N // 2 + 1] = 2
    board[N // 2 + 1][N // 2] = 1
    board[N // 2][N // 2 + 1] = 1

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    cnt_B = 0
    cnt_W = 0
    for i in range(M):
        X, Y, color = map(int, input().split())
        board[X][Y] = color
        if board[X][Y] == 1:
            stackB = []
            for k in range(8):
                cx, cy = X + dx[k], Y + dy[k]
                while 1 <= cx < N + 1 and 1 <= cy < N + 1 and board[cx][cy] == 2:
                    stackB.append([cx, cy])
                    cx, cy = cx + dx[k], cy + dy[k]
                if 1 <= cx < N + 1 and 1 <= cy < N + 1 and board[cx][cy] == 1:
                    for i, j in stackB:
                        board[i][j] = 1
                else:
                    stackB = []
        if board[X][Y] == 2:
            stackW = []
            board[X][Y] = color
            for k in range(8):
                cx, cy = X + dx[k], Y + dy[k]
                while 1 <= cx < N + 1 and 1 <= cy < N + 1 and board[cx][cy] == 1:
                    stackW.append([cx, cy])
                    cx, cy = cx + dx[k], cy + dy[k]
                if 1 <= cx < N + 1 and 1 <= cy < N + 1 and board[cx][cy] == 2:
                    for i, j in stackW:
                        board[i][j] = 2
                else:
                    stackW = []
    for i in range(len(board)):
        cnt_B += board[i].count(1)
        cnt_W += board[i].count(2)

    print(f'#{tc} {cnt_B} {cnt_W}')
