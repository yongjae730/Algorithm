import sys

sys.setrecursionlimit(10 ** 6)

N, M, R = map(int, sys.stdin.readline().split())


def dfs(R):
    global cnt
    visited[R] = cnt
    adjL[R].sort()
    for i in adjL[R]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)


cnt = 1
visited = [0] * (N + 1)
adjL = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())

    adjL[u].append(v)
    adjL[v].append(u)

dfs(R)

for i in range(1, N + 1):
    print(visited[i])
