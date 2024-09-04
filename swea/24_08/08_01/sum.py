for _ in range(1, 11):
    tc = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]

    mx_sum = 0

    for x in range(100):
        total = 0
        for y in range(100):
            total += lst[x][y]
        if mx_sum < total:
            mx_sum = total
    for i in range(100):
        total = 0
        for j in range(100):
            total += lst[j][i]
        if mx_sum < total:
            mx_sum = total
    for k in range(100):
        total = 0
        for l in range(100):
            total += lst[l][l]
        if mx_sum < total:
            mx_sum = total
    for q in range(100):
        total = 0
        for w in range(100-1,-1,-1):
            total += lst[w][w]
        if mx_sum < total:
            mx_sum = total
    print(f'#{tc} {mx_sum}')