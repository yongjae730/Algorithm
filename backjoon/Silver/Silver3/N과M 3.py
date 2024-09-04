def permutation(i, num, M, lst):
    if i == M:
        return print(*lst)

    for j in range(N):
        lst.append(j + 1)
        permutation(i + 1, num, M, lst)
        lst.pop()


N, M = map(int, input().split())
num = []
lst = []
for k in range(1, N + 1):
    num.append(k)

permutation(0, num, M, lst)
