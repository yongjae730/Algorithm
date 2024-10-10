from collections import deque


def houses(x, y):
    # BFS를 위한 큐를 초기화하고 현재 집의 좌표를 큐에 추가
    q = deque()
    q.append([x, y])
    house_lst.append([x, y])  # 시작 집을 집 목록에 추가
    cnt = 0  # 연결된 집의 수를 세기 위한 카운터

    while q:
        # 큐에서 현재 좌표를 꺼냄
        cx, cy = q.popleft()
        cnt += 1  # 집 카운터를 증가시킴

        visited[cx][cy] = True  # 현재 집을 방문한 것으로 표시
        # 상하좌우 네 방향을 체크
        for k in range(4):
            nx, ny = cx + dx[k], cy + dy[k]  # 방향에 따라 새로운 좌표 계산
            # 새로운 좌표가 유효한지 체크
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and downtown[nx][ny] == 1:
                # 유효하다면 큐에 새로운 좌표 추가
                q.append([nx, ny])
                visited[nx][ny] = True  # 새로운 집을 방문한 것으로 표시
                house_lst.append([nx, ny])  # 집 목록에 추가
    return cnt  # 이 연결 요소(타운)의 집 수를 반환


# 그리드에서 이동할 방향: 위, 아래, 왼쪽, 오른쪽
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N = int(input())  # 그리드의 크기를 입력받음

# 다운타운 그리드를 읽음 (1은 집, 0은 빈 땅)
downtown = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]  # 방문한 집을 표시할 그리드 초기화
house_lst = []  # 방문한 집 목록
town_lst = []  # 각 연결 요소(타운)의 크기를 저장할 목록

# 그리드의 각 셀을 순회
for i in range(N):
    for j in range(N):
        # 셀에 집이 있고 방문하지 않았다면
        if downtown[i][j] == 1 and [i, j] not in house_lst:
            # houses 함수를 호출하여 연결된 요소를 탐색
            result = houses(i, j)
            if result != 0:
                town_lst.append(result)  # 타운의 크기를 추가

# 타운의 크기를 정렬
town_lst.sort()
result_lst = []
result_lst.append(len(town_lst))  # 타운의 개수를 첫 번째 요소로 추가
result_lst += town_lst  # 각 타운의 크기를 추가

# 결과 출력
for w in range(len(result_lst)):
    print(result_lst[w])
