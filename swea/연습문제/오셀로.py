T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    othello = [[0 for _ in range(N)] for _ in range(N)]
    a = (N // 2) - 1
    b = (N // 2)
    othello[a][a] = 2
    othello[a][b] = 1
    othello[b][a] = 1
    othello[b][b] = 2
    for _ in range(M):
        X, Y, color = map(int, input().split())
        othello[X - 1][Y - 1] = color
        dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]
        if othello[X - 1][Y - 1] == 1:
            for k in range(8):
                cx, cy = (X - 1) + dx[k], (Y - 1) + dy[k]
                stack = []
                while 0 <= cx < N and 0 <= cy < N and othello[cx][cy] == 2:
                    stack.append((cx, cy))
                    cx, cy = cx + dx[k], cy + dy[k]

                if 0 > cx or cx >= N or 0 > cy or cy >= N or othello[cx][cy] == 0:
                    stack = []
                for i in range(len(stack)):
                    othello[stack[i][0]][stack[i][1]] = 1

        if othello[X - 1][Y - 1] == 2:
            for k in range(8):
                cx, cy = (X - 1) + dx[k], (Y - 1) + dy[k]
                stack = []
                flag = True
                while 0 <= cx < N and 0 <= cy < N and othello[cx][cy] == 1:
                    stack.append((cx, cy))
                    cx, cy = cx + dx[k], cy + dy[k]

                if 0 > cx or cx >= N or 0 > cy or cy >= N or  othello[cx][cy] == 0:
                    stack = []
                for l in range(len(stack)):
                    othello[stack[l][0]][stack[l][1]] = 2
    cnt1 = 0
    cnt2 = 0
    for i in range(N):
        for j in range(N):
            if othello[i][j] == 1:
                cnt1 += 1
            elif othello[i][j] == 2:
                cnt2 += 1

    print(f'#{tc} {cnt1} {cnt2}')
