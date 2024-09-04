# DFS 탐색
def start(maze):
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                return i, j


for tc in range(1, 11):
    T = int(input())
    maze = [list(map(int, input().strip())) for _ in range(16)]

    sti, stj = start(maze)

    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]

    visited = [[0 for _ in range(16)] for _ in range(16)]
    stack = []
    stack.append([sti, stj])
    flag = False
    while len(stack) > 0:
        cx, cy = stack.pop()

        if visited[cx][cy] == 0:
            visited[cx][cy] = 1
            for k in range(4):
                nx, ny = cx + dx[k], cy + dy[k]
                if 0 <= nx < 16 and 0 <= ny < 16 and (maze[nx][ny] == 0 or maze[nx][ny] == 3) and visited[nx][ny] == 0 :
                    stack.append([nx, ny])

        if maze[cx][cy] == 3:
            flag = True

    print(f'#{tc} {int(flag)}')
#########################
# # BFS 탐색
# def start(maze):
#     for i in range(16):
#         for j in range(16):
#             if maze[i][j] == 2:
#                 return i, j
#
# def queue(maze,i,j):
#     global visited
#
#     dx = [1, 0, 0, -1]
#     dy = [0, 1, -1, 0]
#     q = []
#     q.append([i,j])
#     visited[i][j] = 1
#     while len(q) > 0:
#         cx, cy = q.pop(0)
#
#         if maze[cx][cy] == 3:
#             return visited[cx][cy] -1 -1
#
#
#         for k in range(4):
#             nx, ny = cx + dx[k], cy + dy[k]
#             if 0 <= nx < 16 and 0 <= ny < 16 and maze[nx][ny] != 1 and visited[nx][ny] == 0 :
#                 q.append([nx, ny])
#                 visited[nx][ny] = visited[cx][cy] + 1
#
#     return 0
#
# for tc in range(1, 11):
#     T = int(input())
#     maze = [list(map(int, input().strip())) for _ in range(16)]
#     visited = [[0 for _ in range(16)] for _ in range(16)]
#
#     sti, stj = start(maze)
#     queue(maze,sti,stj)
#
#     for i in range(len(visited)):
#         print(visited[i])