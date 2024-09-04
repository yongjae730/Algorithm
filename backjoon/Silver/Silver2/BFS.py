import sys


def BFS(R, visited, e):
    global result
    q = []

    q.append(R)
    visited[R] = 1
    cnt = 1
    while q:
        w = q.pop(0)
        result[w] = cnt
        cnt += 1
        for j in adjL[w]:
            if visited[j] == 0:
                visited[j] = 1
                q.append(j)


N, M, R = map(int, sys.stdin.readline().split())
adjL = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())

    adjL[v].append(u)
    adjL[u].append(v)

for i in range(len(adjL)):
    adjL[i].sort()

result = [0] * (N + 1)
BFS(R, visited, R)

for q in range(1, len(result)):
    print(result[q])
