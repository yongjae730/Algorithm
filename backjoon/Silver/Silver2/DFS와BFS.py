def BFS(V):
    q = []
    q.append(V)
    while q:
        w = q.pop(0)
        visited_bfs[w] = 1
        print(w, end=' ')
        for k in adjL[w]:
            if visited_bfs[k] == 0 and k not in q:
                q.append(k)

def DFS(V):
    visited_dfs[V] = 1
    print(V, end=' ')
    for j in adjL[V]:
        if visited_dfs[j] == 0:
            DFS(j)
    return


N, M, V = map(int, input().split())

adjL = [[] for _ in range(N + 1)]

for i in range(M):
    v, u = map(int, input().split())

    adjL[u].append(v)
    adjL[v].append(u)

for i in range(len(adjL)):
    adjL[i].sort()

visited_dfs = [0] * (N + 1)
visited_bfs = [0] * (N + 1)

DFS(V)
print()
BFS(V)
