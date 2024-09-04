def turn(arr, N):
    arr2 = [[0 for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            arr2[x][y] = arr[N - y - 1][x]

    return arr2


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]

    arr90 = turn(arr, N)
    arr180 = turn(arr90, N)
    arr270 = turn(arr180, N)

    print(f'#{tc}')
    for i in range(N):
        print(''.join(arr90[i]), ''.join(arr180[i]), ''.join(arr270[i]))
