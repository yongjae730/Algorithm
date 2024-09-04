import sys
sys.stdin = open('input (8).txt')



def path(x):
    visited[x] = True

    if adj[x] != -1:
        nxt = adj[x]
        if visited[nxt] == False:
            path(nxt)
    if adj2[x] != -1:
        nxt = adj2[x]
        if visited[nxt] == False:
            path(nxt)


for tc in range(1, 11):
    N, M = map(int, input().split())

    adj = [-1] * 101
    adj2 = [-1] * 101

    node = list(map(int, input().split()))

    for i in range(0, len(node), 2):
        if adj[node[i]] != -1:
            adj2[node[i]] = node[i + 1]
        elif adj[node[i]] == -1:
            adj[node[i]] = node[i + 1]

    visited = [False] * 101

    path(0)

    print(visited[99])




    # for nxt in [adj[x], adj2[x]]:
    #     if nxt != -1:
    #         if visited[nxt] == False:
    #             path(nxt)