for tc in range(1,11):
    N = int(input())
    arr = [list(map(int,input().split()))for _ in range(100)]
    n = 1
    s = 2

    cnt = 0
    for y in range(100):
        flag = False
        for x in range(100):
            if arr[x][y] == 1:
                flag = True
            elif arr[x][y] == 2 and flag == True:
                cnt += 1
                flag = False
    print(f'#{tc} {cnt}')
