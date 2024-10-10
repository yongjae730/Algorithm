import sys
from collections import deque


def maze_bfs(x, y):
    # BFS를 위한 큐를 초기화하고 시작 좌표를 큐에 추가
    q = deque()
    q.append([x, y])
    visited[x][y] = 1  # 시작 위치를 방문한 것으로 표시

    while q:
        # 큐에서 현재 좌표를 꺼냄
        cx, cy = q.popleft()
        # 상하좌우 네 방향을 체크
        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]  # 새로운 좌표 계산
            # 새로운 좌표가 유효한지 체크
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1:
                # 새로운 좌표가 방문하지 않았고, 이동할 수 있는 위치인 경우
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[cx][cy] + 1  # 현재 위치에서 1을 더한 값을 저장
                    q.append([nx, ny])  # 새로운 좌표를 큐에 추가


# 상하좌우 이동을 위한 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N, M = map(int, input().split())  # 미로의 크기를 입력받음
maze = [list(map(int, input().strip())) for _ in range(N)]  # 미로 정보를 입력받음 (1은 통로, 0은 벽)
visited = [[False for _ in range(M)] for _ in range(N)]  # 방문 여부를 기록할 그리드 초기화

maze_bfs(0, 0)  # (0, 0)에서 BFS 시작
result = visited[N - 1][M - 1]  # 도착 위치의 방문 기록을 가져옴
print(result)  # 도착 지점까지의 최소 이동 거리를 출력
