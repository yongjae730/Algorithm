T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bi = list(map(int, input().split()))
    max_num = -9999
    if N <= M:
        for j in range(0,M-N+1):
            num = 0
            for i in range(N):
                num += Ai[i]*Bi[i+j]
            if num > max_num:
                max_num = num
    if N > M:
        for j in range(0,N-M+1):
            num = 0
            for i in range(M):
                num += Ai[i+j]*Bi[i]
            if num > max_num:
                max_num = num

    print('#{} {}'.format(tc,max_num))