'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''


# make_set : 자기 자신으로 부모를 초기화(나 자신만 포함하는 단독집합) 하는 연산
def make_set(N):
    return list(range(N))


# find_set : 해당 노드 x의 대표자(최상위 부모)를 찾는 연산
def find_set(parents, x):
    # 기저조건 : 부모가 자기 자신이면 종료
    if parents[x] == x:
        return x
    # 유도 조건
    # 경로 압축 (Path compression)
    parents[x] = find_set(parents, parents[x])
    return parents[x]


# union : 요소  x와 요소 y가 속한 그룹을 하나의 그룹으로 통합할 때 연산
def union(parents, x, y):
    root_x = find_set(parents, x)
    root_y = find_set(parents, y)

    if root_x != root_y:
        parents[root_x] = root_y


# 크루스칼 알고리즘으로 최소 신장 트리를 구하기
def kruskal(adj, V):
    # 최소비용을 가지고 있는 가중치를 선택하며, (사이클이 발생하지 않는 선에서)
    # V-1 개 만큼 간선을 선택 -< MST 된다!
    # 간선 배열[(시작점, 끝점, 가중치)]
    edges = []
    for v in range(V):  # 시작점 v
        for u, w in adj[v]:  # 끝점 u
            edges.append((v, u, w))

    edges.sort(key=lambda x: x[2])  # 간선을 가중치 기준 정렬
    mst = []  # 간선 최소 비용을 저장할 배열
    parents = make_set(V)
    for v, u, w in edges:
        # 사이클을 형성하는지 확인 (union-find 알고리즘)
        if find_set(parents,v) != find_set(parents, u):  # 싸이클이 형성된다x == 같은 그룹에 속한다x
            mst.append(w)
            union(parents, u, v)
    return mst


# 정점 수 V, 간선 수 E
V, E = map(int, input().split())

# 인접 리스트 초기화
adj = [[] for _ in range(V)]

# 간선의 정보를 입력 받기

for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))  # u -> v : w
    adj[v].append((u, w))  # v -> u : w

start_node = 0
MST = kruskal(adj, V)

print(MST)
print("총합 ", sum(MST))
