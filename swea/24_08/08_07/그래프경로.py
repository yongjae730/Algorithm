def dfs(v):

    visited[v] = 1
    for i in adj[v]:
        if visited[i] == 1:
            continue

        dfs(i)



T = int(input())

for tc in range(1,T+1):
    V,E = map(int,input().split())
    adj = [[]for _ in range(V+1)]
    for i in range(E):
        v,u = map(int,input().split())
        adj[v].append(u)
    S,G = map(int,input().split())

    visited = [0] *(V+1)
    dfs(S)
    print(f'#{tc} {visited[G]}')
