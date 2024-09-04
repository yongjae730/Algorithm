import sys

sys.setrecursionlimit(10 * 6)


def permutation(i, num, M, lst):
    if i == M:
        return print(*lst)

    for j in range(N):
        lst.append(num[j])
        permutation(i + 1, num, M, lst)
        lst.pop()


N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
num.sort()
lst = []
visited = [0] * (N + 1)

permutation(0, num, M, lst)
