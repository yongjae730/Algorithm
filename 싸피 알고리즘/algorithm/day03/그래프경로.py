def graph(v):

    visited[v] = 1

    for u in adj[v]:
        if visited[u] == 1:
            continue

        graph(u)


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[] for i in range(V + 1)]
    for i in range(E):
        v, u = map(int, input().split())

        adj[v].append(u)
    S, G = map(int, input().split())
    print(adj)
    visited = [0] * (V + 1)

    graph(S)

    print(f'#{tc} {visited[G]}')
