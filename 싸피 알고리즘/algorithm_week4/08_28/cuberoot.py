T = int(input())

for tc in range(1,T+1):
    N = int(input())

    num = 0
    A = 0
    while A < N:

        num += 1
        A = num*num*num

    if A == N :
        print(f'#{tc} {num}')
    else:
        print(f'#{tc} -1')