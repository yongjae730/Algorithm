T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())  # N = 사람 수, M초의 시간 동안 K개의 붕어빵을 만듬
    customer = list(map(int, input().split()))

    fish = 0
    time = 0
    cnt = 0
    flag = True
    while flag == True and cnt < len(customer):

        if time > 0 and time % M == 0:
            fish += K

        for i in range(N):
            if customer[i] == time and fish != 0:
                fish -= 1
                cnt += 1
            elif customer[i] > time:
                continue
            elif customer[i] < time:
                continue
            elif customer[i] == time and fish == 0:
                flag = False

        time += 1

    if cnt == len(customer):
        print(f'#{tc} Possible')
    else:
        print(f'#{tc} Impossible')
