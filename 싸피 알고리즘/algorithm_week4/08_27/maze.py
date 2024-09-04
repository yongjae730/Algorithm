def start(maze):

    for x in range(16):
        for y in range(16):
            if maze[x][y] == 2:
                return x, y


def check(maze):
    stx, sty = start(maze)
    visited = [[0 for _ in range(16)] for _ in range(16)]
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]

    q = []
    q.append([stx, sty])

    while q:
        cx, cy = q.pop(0)
        visited[cx][cy] = 1
        if maze[cx][cy] == 3:
            return 1
        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]
            if 0 <= nx < 16 and 0 <= ny < 16 and maze[nx][ny] != 1 and visited[nx][ny] == 0:
                q.append([nx,ny])

    return 0


T = 10

for _ in range(1, T + 1):
    tc = int(input())
    maze = [list(map(int, input().strip())) for _ in range(16)]

    print(f'#{tc} {check(maze)}')