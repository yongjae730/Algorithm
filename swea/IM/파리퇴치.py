T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    mx_flies = 0
    for x in range(N-M+1):
        for y in range(N-M+1):
            sum_flies = 0
            for i in range(M):
                for j in range(M):
                    sum_flies += arr[x+i][y+j]

            if mx_flies < sum_flies:
                mx_flies = sum_flies
    print(f'#{tc} {mx_flies}')