# 길찾기
# 입력
# 총 10개의 테스트 케이스가 주어진다.
T = 10
for _ in range(1, T + 1):
    # 각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호와 길의 총 개수가 공백으로 분리되어 주어진다.
    tc, N = map(int, input().split())  # ["1", "16"]
    # 그 다음 줄에는 순서쌍이 주어진다. 순서쌍의 경우, 별도로 나누어 표현되는 것이 아니라 숫자의 나열이며, 나열된 순서대로 순서쌍을 이룬다.
    arr = list(map(int, input().split()))

    # 인접리스트 생성
    # 도시(정점)의 갯수 V
    V = 100
    adj = [[] for _ in range(V)]
    for idx in range(0, len(arr), 2):
        v = arr[idx]
        u = arr[idx + 1]
        # v -> u
        adj[v].append(u)

    # 로직 (DFS 탐색, 완전탐색을 통해서 0부터 시작하는 모든 경로 다 탐색)
    # 방문검사 배열 (중복순회 방지)
    visited = [False] * V


    # DFS 탐색 진행
    def dfs(start):
        # 방문 체크 (현재 도시)
        visited[start] = True
        # 재귀호출
        # 인접된 도시를 방문 (방문하지 않았다면)
        for nxt in adj[start]:
            if visited[nxt] == True:
                continue
            dfs(nxt)


    dfs(0)

    # visited 배열의 99번 도시에 해당하는 값이... True 가 되어 있다면
    # 0 -> ... -> 99 경로가 있다!
    if visited[99] == True:
        result = 1
    else:
        result = 0
    # 출력
    print(f"#{tc} {result}")
