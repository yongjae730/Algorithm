T = int(input())

for i in range(1,T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    mx_num = 0
    mn_num = 9999999999999999
    for j in range(0, N-M+1):
        sum_num = 0
        for k in range(M):
            sum_num += lst[j+k]

        if sum_num > mx_num:
                mx_num = sum_num

        if sum_num < mn_num:
                mn_num = sum_num

    print(f'#{i} {mx_num-mn_num}')