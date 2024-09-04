def squre(N,K,A,i):
    if i == K:
        return A

    return squre(N,K,A*N,i+1)



for _ in range(10):
    tc = int(input())
    N,K = map(int,input().split())
    A = N

    print(f'#{tc} {squre(N,K,A,1)}')

