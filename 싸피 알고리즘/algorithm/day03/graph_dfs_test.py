# 인접 리스트 : 그래프 표현
# 현재 정점(도시) i를 기준으로 해서
# 인접(연결)되어 있는 다음 도시 j의 관계를 표현
# 도시의 갯수 N
N = 7
# 인접 리시트를 초기화 adj
adj = [[] for i in range(N + 1)]

# 인접 되어 있는 도시 정보를 추가(갱신)
text = '1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7'
arr = list(map(int, text.split(', ')))
for i in range(0, len(arr), 2):
    v = arr[i]  # 도시 v
    u = arr[i + 1]  # 도시 u
    # v <-> u 가 서로 인접(연결) 되어있다.
    adj[v].append(u)  # 도시 v -> 도시 u
    adj[u].append(v)  # 도시 u -> 도시 v

# DFS 탐색(재귀함수)
# 방문체크를 위한 배열 visited
visited = [False] * (N + 1)


def dfs(v):  # 시작정점 v
    # 시작 정점v에 대한 방문 체크
    visited[v] = True
    print(f'-{v}',end = '')
    print(end='')
    # 인접되어 있는 나머지 도시(정점)을 방문...!(재귀)
    # 현재 나의 도시 v로부터 인접되어있는 도시 -> adj[v]
    for u in adj[v]:  # 인접되어 있는 도시 u
        # 해당 도시 u에 대해 방문을 진행했는지 확인 (기저조건)
        if visited[u] == True:
            continue
        # 아직 방문하지 않은 u도시 인경우..(재귀호출)
        dfs(u)


dfs(1)  # 1번을 시작으로 DFS 탐색 시작
