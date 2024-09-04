import sys
sys.stdin = open('../input/1209.txt')

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    mx_total = 0

    for i in range(100):
        total = 0
        for j in range(100):
            total += arr[i][j]
        mx_total = max(total, mx_total)

    arr = list(map(list, zip(*arr)))  # ->
    for i in range(100):
        total = 0
        for j in range(100):
            total += arr[i][j]
        mx_total = max(total, mx_total)

    total = 0
    for i in range(100):
        total += arr[i][i]
    mx_total = max(total, mx_total)

    total = 0
    for i in range(100):
        total += arr[i][100 - i - 1]
    mx_total = max(total, mx_total)

    print(f'#{tc} {mx_total}')