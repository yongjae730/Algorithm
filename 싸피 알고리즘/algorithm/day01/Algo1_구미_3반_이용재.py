T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    bacterias = [list(map(int, input().split())) for _ in range(N)]
    dy = [1, 0, 0, -1] # x방향 탐색 범위
    dx = [0, 1, -1, 0] # y방향 탐색 범위
    max_food = 0 # 최대 음식 량

    for x in range(N):
        for y in range(N):
            food = bacterias[x][y] # 탐색 시작지점의 음식량
            for k in range(4):
                cx, cy = x + dx[k], y + dy[k]
                if 0 <= cx < N and 0 <= cy < N: # 범위밖의 탐색을 막기위한 범위설정
                    food += bacterias[cx][cy] #시작지점의 음식량에 4방향의 음식량을 더해줌
            if max_food == 0:
                max_food = food
            if max_food < food:
                max_food = food

    print(f'#{tc} {max_food}')
