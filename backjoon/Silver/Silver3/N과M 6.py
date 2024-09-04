import sys

sys.setrecursionlimit(10 * 6)


def permutation(i, num, M, lst, q):
    if i == M:
        return print(*lst)

    for j in range(q, N):
        if visited[j] == 0:
            visited[j] = 1
            lst.append(num[j])
            permutation(i + 1, num, M, lst, j)
            lst.pop()
            visited[j] = 0


N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
num.sort()
lst = []
visited = [0] * (N + 1)

permutation(0, num, M, lst, 0)
