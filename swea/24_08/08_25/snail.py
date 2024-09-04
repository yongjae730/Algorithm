T = int(input())

for tc in range(1, T + 1):
    N, K = map(int,input().split())
    board = list(map(int,input().split()))

    power = K-1
    cnt = 1
    for i in range(N):
        if board[i] == 1:
            power = K-1
            cnt += 1
        elif board[i] == 0:
            if power == 0:
                break
            else:
                cnt += 1
                power -= 1

    if cnt >= N:
        print(f'#{tc} {N}')
    else:
        print(f'#{tc} {cnt}')
