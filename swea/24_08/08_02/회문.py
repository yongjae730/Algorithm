def check(board, N, M):
    for x in range(N):
        for y in range(N-M+1):
            if board[x][y]  == board[x][M-y-1]:
                return print(board[x])
    return print('No')



T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(str, input().strip())) for _ in range(N)]

    check(board, N, M)
