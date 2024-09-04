import sys
sys.setrecursionlimit(10**6)


def tree(node,depth):

    for j in adjL[node]:
        if visited[j] == 0:
            visited[j] = node
            tree(j,depth+1)


N = int(sys.stdin.readline())

adjL = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(N - 1):
    v, u = map(int, sys.stdin.readline().split())

    adjL[v].append(u)
    adjL[u].append(v)

tree(1,1)

for i in range(2, N + 1):
    print(visited[i])

# dp 방식으로 풀면 recursionlimit을 안써도 된다
