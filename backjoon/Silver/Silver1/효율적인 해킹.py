from collections import deque

def check(V):
    visited = [False] * (N + 1)

    q = deque()
    q.append(V)
    cnt = 0
    visited[V] = True
    while q:
        v = q.popleft()

        for w in adj[v]:
            if visited[w] == False:
                visited[w] = True
                q.append(w)
                cnt += 1
    return cnt

N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]

for _ in range(M):
    v, u = map(int, input().split())
    adj[u].append(v)

lst = []

for i in range(1, N + 1):
    lst.append(check(i))

mx = max(lst)

for j in range(len(lst)):
    if lst[j] == mx:
        print(j + 1, end=' ')
