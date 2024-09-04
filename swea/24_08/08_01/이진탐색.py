def search(N, P):
    start = 1
    end = P
    cnt = 0

    while start < end:
        cnt += 1
        middle = (start + end) // 2
        if middle == N:
            return cnt
        if middle < N:
            start = middle
        elif middle > N:
            end = middle

    return cnt


T = int(input())

for i in range(1, T + 1):
    P, A, B = map(int, input().split())

    acnt = search(A, P)
    bcnt = search(B, P)

    if acnt > bcnt:
        print('B')
    elif bcnt > acnt:
        print('A')
    else:
        print(0)
