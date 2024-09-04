T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    customer = list(map(int, input().split()))

    time = 0
    fish = 0
    cnt = 0
    flag = True
    while flag == True and cnt < len(customer):

        if time > 0 and time % M == 0:
            fish += K

        for i in range(len(customer)):
            if time == customer[i]:
                if fish == 0:
                    flag = False
                else:
                    fish -= 1
                    cnt += 1

        time += 1

    if flag == True:
        print(f'#{tc} Possible')
    else:
        print(f'#{tc} Impossible')

