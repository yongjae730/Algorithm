def check(N, i, sum_num, visited):
    global mn_num
    if i == N:

        if sum_num < mn_num:
            mn_num = sum_num
            return mn_num
        elif mn_num < sum_num:
            return

    for j in range(N):
        if visited[j] == 0:

            visited[j] = 1

            check(N, i + 1, sum_num + arr[i][j], visited)

            visited[j] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    mn_num = 999
    check(N, 0, 0, visited)
    print(mn_num)
