import sys

sys.setrecursionlimit(10 * 6)


def permutation(i, num, M, lst,q):

    global stack
    if i == M:
        if tuple(lst) not in stack:
            stack.add(tuple(lst))
            print(*lst)
            return
        return

    for j in range(q,N):
        lst.append(num[j])
        permutation(i + 1, num, M, lst,q)
        lst.pop()

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
num.sort()
lst = []
stack = set()
visited = [0] * (N + 1)

permutation(0, num, M, lst,0)
