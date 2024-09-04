M, N = map(int, input().split())  # 6 4
box = [list(map(int, input().split())) for _ in range(N)]

# 로직(BFS 탐색을 통해서 주변에 있는 토마토를 익게 만들겠다!)
# BFS를 진행하기 위한 큐 자료형
queue = []
# 방문 체크 배열
visited = [[False] * M for _ in range(N)]
# 익은 토마토의 좌표를 큐에 담아주기
for i in range(N):
    for j in range(M):
        # 익은 토마토다!
        if box[i][j] == 1:
            # 큐에 해당 좌표를 담아준다!
            queue.append([i, j])
            visited[i][j] = True

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

cnt = -1  # 현재 시간
# BFS 탐색 => 인접되어 있는 안익은 토마토들을 익게 만들겠다!
while len(queue) > 0:
    # 큐 안의 요소의 갯수를 측정
    q_size = len(queue)
    for _ in range(q_size):
        # 익은 토마토를 하나 꺼내겠다! 좌표 : (ci, cj)
        ci, cj = queue.pop(0)
        box[ci][cj] = 1  # 익은 토마토로 변경

        # 익은 토마토를 기준으로 하여,,, 주변에 있는 안익은 토마토 익게!
        # 사방탐색 (상하좌우)
        for k in range(4):
            ni = ci + di[k]
            nj = cj + dj[k]
            # 해당 좌표가 범위 바깥을 나간 경우이거나,
            # 해당 좌표에 익지 않은 토마토가 아니라면...!
            # 다음 탐색을 계속해서 진행!
            if ni < 0 or ni >= N or nj < 0 or nj >= M or box[ni][nj] != 0 or visited[ni][nj] == True:
                continue

            # 안익은 토마토의 좌표 : (ni, nj)
            # 다음 탐색할 토마토를 위해 큐에 삽입!
            queue.append((ni, nj))
            visited[ni][nj] = True
    cnt += 1

# 모든 토마토가 익었는지 확인!
for i in range(N):
    for j in range(M):
        # 익지 않은 토마토가 발견이 된다면
        if box[i][j] == 0:
            print(-1)
            exit()

print(cnt)
