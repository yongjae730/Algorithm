T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = []
    for _ in range(N):
        A, B = map(int, input().split())
        lst.append([A, B])
    lst.sort()
    cnt = 0
    for i in range(N):
        for j in range(i+1,N):
            if lst[i][1] > lst[j][1]:
                cnt += 1
    print(f'#{tc} {cnt}')
