from heapq import heappop, heappush


def dijkstra(N, field):
    # 상하좌우 이동을 위한 방향 벡터
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 최소 힙을 사용하여 (현재까지의 거리, x, y) 튜플을 저장
    mn_heap = [(0, 0, 0)]  # (거리, x, y)

    # 거리 정보를 무한대로 초기화
    dist = [[float('inf')] * N for _ in range(N)]
    dist[0][0] = 0  # 시작점의 거리는 0

    while mn_heap:
        # 현재까지의 거리와 위치를 힙에서 꺼냄
        current_dist, x, y = heappop(mn_heap)

        # 목표 지점에 도달한 경우, 현재까지의 거리를 반환
        if x == N - 1 and y == N - 1:
            return current_dist

        # 상하좌우 네 방향으로 이동
        for i in range(4):
            nxt_x, nxt_y = x + dx[i], y + dy[i]
            # 이동이 가능한 위치인지 확인
            if 0 <= nxt_x < N and 0 <= nxt_y < N:
                # 현재 위치에서 다음 위치까지의 거리 계산
                fuel = dist[x][y] + max(0, (field[nxt_x][nxt_y] - field[x][y])) + 1
                # 더 짧은 거리가 발견된 경우 거리 업데이트 및 힙에 추가
                if dist[nxt_x][nxt_y] > fuel:
                    dist[nxt_x][nxt_y] = fuel
                    heappush(mn_heap, (fuel, nxt_x, nxt_y))  # (거리, x, y)

    # 목표 지점까지의 최단 거리를 반환
    return dist[N - 1][N - 1]


# 테스트 케이스의 개수 입력
T = int(input())
for tc in range(1, T + 1):
    # 격자의 크기 입력
    N = int(input())
    # 격자의 각 행을 입력받아 2D 리스트 생성
    field = [list(map(int, input().split())) for _ in range(N)]

    # 다익스트라 알고리즘 실행 및 결과 출력
    result = dijkstra(N, field)
    print(f'#{tc} {result}')
