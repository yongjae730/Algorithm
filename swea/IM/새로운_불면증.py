T = int(input())

for tc in range(1,T+1):
    N = int(input())
    set_N = set()
    cnt = 1
    while len(set_N) < 10:
        S = cnt * N

        for i in str(S):
            set_N.add(i)
        cnt += 1

    print(f'#{tc} {S}')