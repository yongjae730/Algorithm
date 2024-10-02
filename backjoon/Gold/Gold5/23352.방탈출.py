from collections import deque
import sys


def bfs(x, y):
    visited = [[0] * M for _ in range(N)]
    length = 0
    result = 0
    result_lst = []
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        cx, cy = q.popleft()
        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] != 0 and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[cx][cy] + 1

        if visited[cx][cy] > length:
            result_lst = []
            result = board[x][y] + board[cx][cy]
            length = visited[cx][cy]
            result_lst.append(result)

        elif visited[cx][cy] == length:
            result = board[x][y] + board[cx][cy]
            result_lst.append(result)

    return max(result_lst),length


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

total = []
mx_len = 0

for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            continue
        cnt,len = bfs(i, j)
        if len > mx_len:
            total = []
            mx_len = len
            total.append(cnt)
        elif len == mx_len:
            total.append(cnt)

print(max(total))