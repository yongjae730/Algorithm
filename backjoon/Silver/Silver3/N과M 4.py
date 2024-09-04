import sys

sys.setrecursionlimit(10 * 6)


def permutation(i, num, M, lst,q):
    if i == M:
        return print(*lst)

    for j in range(q,N):
        lst.append(j + 1)
        permutation(i + 1, num, M, lst,j)
        lst.pop()


N, M = map(int, sys.stdin.readline().split())
num = []
lst = []
for k in range(1, N + 1):
    num.append(k)

permutation(0, num, M, lst,0)
