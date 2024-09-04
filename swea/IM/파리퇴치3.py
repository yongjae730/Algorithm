T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    fly_arr = [list(map(int, input().split())) for _ in range(N)]

    dx1 = [-1, 0, 1, 0]
    dy1 = [0, 1, 0, -1]
    dx2 = [-1, 1, -1, 1]
    dy2 = [-1, -1, 1, 1]
    mx_fly = 0
    for x in range(N):
        for y in range(N):
            fly = fly_arr[x][y]
            for i in range(1, M):
                for k in range(4):
                    cx, cy = x + dx1[k]*i, y + dy1[k]*i
                    if 0 <= cx < N and 0 <= cy < N:
                        fly += fly_arr[cx][cy]
            if fly >= mx_fly:
                mx_fly = fly

    for x in range(N):
        for y in range(N):
            fly = fly_arr[x][y]
            for i in range(1,M):
                for k in range(4):
                    cx, cy = x + dx2[k]*i, y + dy2[k]*i
                    if 0 <= cx < N and 0 <= cy < N:
                        fly += fly_arr[cx][cy]
            if fly >= mx_fly:
                mx_fly = fly
    print(f'#{tc} {mx_fly}')
