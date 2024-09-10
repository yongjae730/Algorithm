data = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

# 인접 행렬
# V x V 크기의 이차원 배열을 사용하여 간선의 정보를 저장
V = 7
matrix = [[0] * (V + 1) for _ in range(V + 1)]
for idx in range(0, len(data), 2):
    v = data[idx]
    u = data[idx + 1]
    # 무방향 그래프 u -> v, v -> u
    matrix[v][u] = 1  # v -> u 연결되어 있음을 표시
    matrix[u][v] = 1  # u -> v 연결되어 있음을 표시

print()

# 인접 리스트
# 각 정점에 대해서 인접해 있는 간선 정보를 저장
adj = [[] for _ in range(V + 1)]
for idx in range(0, len(data), 2):
    v = data[idx]
    u = data[idx + 1]
    # 무방향 그래프 u -> v, v -> u
    adj[v].append(u)  # u -> v
    adj[u].append(v)  # v -> u
print()


# DFS 탐색( 완전 탐색, 깊이 우선 탐색)
# 해당 정점에서 시작해서 더 이상 탐색할 수 없을 때까지 깊게 탐색진행
# 방문 체크가 필요! why? 이미 방문했던 노드를 재탐색 하지않기 위해
def dfs(current_node):
    visited[current_node] = 1
    print(current_node, end="-")
    # 유도조건 : 재귀의 형태로 다음 노드 방문
    # 인접 되어 있는 노드 정보를 가져와서 탐색 수행
    for nxt_node in adj[current_node]:
        if visited[nxt_node] == 0:
            dfs(nxt_node)


visited = [0 for _ in range(V + 1)]
dfs(1) # 1번 노드를 시작으로 탐색 시작
print()
# BFS 탐색(완전 탐색, 너비우선 탐색)
# 해당 정점에서 시작하여 인접되어 있는 정점들을 순차적으로 탐색진행
# 방문 체크가 필요! why? 이미 방문했던 노드를 재탐색 하지않기 위해


visited = [0 for _ in range(V + 1)]


def BFS(current_node):
    visited[current_node] = 1

    q = []
    q.append(current_node)

    while q:
        current_node = q.pop(0)
        print(current_node,end="-")
        for nxt_node in adj[current_node]:
            if not visited[nxt_node]:
                q.append(nxt_node)
                visited[nxt_node] = 1

BFS(1)

