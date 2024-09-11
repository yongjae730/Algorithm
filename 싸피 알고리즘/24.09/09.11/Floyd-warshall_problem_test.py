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


# 모든 정점 -> 모든 정점 최소 비용 :  VxV 이차원 배열이 나온다
def floyd_warshall(matrix, V):
    # 최소 경로 비용 이차원 배열
    dist = [[float("inf")] * V for _ in range(V)]
    # 최소 경로 비용이 자기 자신으로 가게되는 비용은 0!
    for i in range(V):
        dist[i][i] = 0

    for u in range(V):
        for v in range(V):
            if u != v:
                dist[u][v] = matrix[u][v]

    # i,j,k 정점 (모든 정점에 대해서 순회 가능)
    # i -> j : i-> k -> j 경로 갱신

    # 징검다리 역할을 하는 k 정점
    for k in range(V):
        # (i->j) 쌍을 순회
        for i in range(V):
            for j in range(V):
                # i->j >> i -> k -> j 갱신
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# 인접 행렬 : 이차원 배열에 각 간선의 정보를 기록하는 방식
# 정점의 개수 V와 간선의 갯수 E
V, E = map(int, input().split())

matrix = [[float("inf")] * V for _ in range(V)]

# 간선의 정보 u -> v : w
# -> matrix[u][v] = w
for _ in range(E):
    u, v, w = map(int, input().split())
    matrix[u][v] = w
    matrix[v][u] = w

dist = floyd_warshall(matrix, V)

from pprint import pprint
pprint(dist)