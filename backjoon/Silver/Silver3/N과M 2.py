def permutation(i, num, visited, M, lst):
    if i == M:
        for q in range(len(lst) - 1):
            if lst[q] > lst[q + 1]:
                return
        return print(*lst)

    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            lst.append(j + 1)
            permutation(i + 1, num, visited, M, lst)
            lst.pop()
            visited[j] = 0


N, M = map(int, input().split())
num = []
visited = [0] * N
lst = []
for k in range(1, N + 1):
    num.append(k)

permutation(0, num, visited, M, lst)
