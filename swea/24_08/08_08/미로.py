def start(maze):
    for x in range(N):
        for y in range(N):
            if maze[x][y] == 2:
                return x, y


def check(maze, stx, sty):
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    stack = []

    stack.append([stx, sty])

    while stack:
        cx, cy = stack.pop()
        visited[cx][cy] = 1
        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]
            if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] != 1 and visited[nx][ny]!=1:
                stack.append([nx, ny])
                if maze[nx][ny] == 3:
                    return True
    return False


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input().strip())) for _ in range(N)]

    stx, sty = start(maze)

    print(f'#{tc} {int(check(maze, stx, sty))}')
