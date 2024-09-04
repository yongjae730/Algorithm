T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flies = [list(map(int,input().split())) for _ in range(N)]

    max_flies = 0
    for x in range(N-M+1):
        for y in range(N-M+1):
            zone = 0
            for k in range(M):
                for l in range(M):
                    zone += flies[x+k][y+l]
            if zone>max_flies:
                max_flies = zone
    print(f'#{tc} {max_flies}')
