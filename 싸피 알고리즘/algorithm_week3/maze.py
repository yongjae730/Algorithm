def start_point(maze, N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input().strip())) for _ in range(N)]

    sti, stj = start_point(maze, N)

    visited = [[0 for _ in range(N)] for _ in range(N)]
    q = []
    q.append([sti, stj])
    visited[sti][stj] = 1
    cnt = 0

    while q:

        ti, tj = q.pop(0)
        di = [1, 0, 0, -1]
        dj = [0, 1, -1, 0]
        if maze[ti][tj] == 3:
            cnt += visited[ti][tj] - 1 - 1

        for k in range(4):
            wi, wj = ti + di[k], tj + dj[k]
            if 0 <= wi < N and 0 <= wj < N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                q.append([wi, wj])
                visited[wi][wj] = visited[ti][tj] + 1

    print(f'#{tc} {cnt}')
