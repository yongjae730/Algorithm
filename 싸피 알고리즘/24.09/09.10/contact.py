import sys

sys.stdin = open('input.txt')


def bfs(start):
    q = []
    q.append(start)
    depth[start] = 1
    while q:
        v = q.pop(0)
        for i in adjL[v]:
            if visited[i] == False:
                visited[i] = True
                depth[i] = depth[v] + 1
                q.append(i)


for tc in range(1, 11):
    length, start = map(int, input().split())
    arr = list(map(int, input().split()))
    adjL = [[] for _ in range(101)]
    visited = [False] * 101
    depth = [0] * 101
    for i in range(0, len(arr), 2):
        v = i
        u = i + 1

        adjL[arr[v]].append(arr[u])

    bfs(start)
    mx_depth = -1e9
    result = 0
    for j in range(len(depth)):
        if depth[j] >= mx_depth:
            mx_depth = depth[j]
            result = j
    print(f'#{tc} {result}')
