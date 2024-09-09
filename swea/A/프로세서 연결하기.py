import sys

sys.stdin = open('input.txt', 'r')


def find_core(board):
    for x in range(N):
        for y in range(N):
            if board[x][y] == 1:
                cores.append([x, y])
    return


def check_core_priority(cores):
    for i in range(len(cores)):
        x, y = cores[i]
        cnt = 4
        for k in range(4):
            cx, cy = x + dx[k], y + dy[k]
            while 0 <= cx < N and 0 <= cy < N:
                if board[cx][cy] == 1:
                    cnt -= 1
                    break
                cx, cy = cx + dx[k], cy + dy[k]
        if cnt != 0:
            cores_priority.append([x, y, cnt])


def check_length(core_lst):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(len(core_lst)):
        x, y, priority = core_lst.pop()
        mn_length = 1e9
        short_stack = []
        if x == 0 or x == N - 1 or y == 0 or y == N - 1:
            continue

        for k in range(4):
            cx, cy = x + dx[k], y + dy[k]
            stack = []
            cnt = 0
            while 0 <= cx < N and 0 <= cy < N:
                if board[cx][cy] == 0:
                    stack.append([cx, cy])
                    visited[cx][cy] = 1
                    cnt += 1
                else:
                    stack = []
                    cnt = 1e9
                    break
                cx, cy = cx + dx[k], cy + dy[k]
            if cnt <= mn_length:
                mn_length = cnt
                short_stack = []
                for j in range(len(stack)):
                    short_stack.append(stack[j])
        if len(short_stack):
            for k in range(len(short_stack)):
                nx, ny = short_stack[k]

                board[nx][ny] = 2


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    cores = []
    find_core(board)
    cores_priority = []
    check_core_priority(cores)

    core_lst = sorted(cores_priority, key=lambda x: (-x[2], x[0]))
    check_length(core_lst)
    result = 0
    for i in range(N):
        result += board[i].count(2)
    print(f'#{tc} {result}')
