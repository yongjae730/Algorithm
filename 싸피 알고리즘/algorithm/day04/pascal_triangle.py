T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    triangle = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        triangle[i][0] = 1
        triangle[i][i] = 1
    for i in range(2,N):
        for j in range(1,N):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    print(f'#{tc}')
    for i in range(N):
        print(*triangle[i][:i + 1])
