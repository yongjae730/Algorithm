T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    arr = list(map(int,input().split()))

    # 현재 위치
    place = 0
    # 갈 수 있는 힘
    power = K

    for i in range(N):

        # 힘이 없으면 멈춘다
        if power == 0 :
            break
        # 0이면 힘 -1 위치 +1
        elif arr[i] == 0:
            power -= 1
            place += 1
        # 1이면 힘 충전, 위치 +1
        elif arr[i] == 1:
            power = K
            place += 1

    print(f'#{tc} {place}')
