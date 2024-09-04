import sys

sys.stdin = open('in.txt')

# 한변의 길이
N = int(input())  # 3
# 이차원 배열의 NxN크기의 배열
arr2d = [list(map(int, input().split())) for _ in range(N)]

print(arr2d)
# 한 변의 길이 N
N = int(input())

arr2d = [list(map(int, input())) for _ in range(N)]

print(arr2d)

# 행 우선순회 (가로 먼저)
for i in range(N):  # i행 (row)
    for j in range(N):  # j열 (col)
        print(arr2d[i][j], end = ' ')
print()


#열 우선 순위 (세로 먼저)
for j in range(N):  # j열 (col)
    for i in range(N):  # i행 (row)
        print(arr2d[i][j], end = ' ')
print()

















