import sys

sys.stdin = open('../input/1961.txt')


def rotate_arr(arr):
    rotated_arr = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            rotated_arr[i][j] = arr[N - 1 - j][i]

    return rotated_arr


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    rotate90 = rotate_arr(arr)
    rotate180 = rotate_arr(rotate90)
    rotate270 = rotate_arr(rotate180)
    print(f'#{tc}')
    for i in range(N):
        print(*rotate90[i], sep='', end=' ')
        print(*rotate180[i], sep='', end=' ')
        print(*rotate270[i], sep='')
