# 사방탐색 : 델타 탐색 중에서도 상하좌우를 탐색하는 방법
# arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# N = 3

# # 열 우선 순회
# for i in range(N):
#     for j in range(N):
#         # print(arr[i][j])
#         # 상 (i-1, j)
#         ci, cj = i - 1, j
#         # 범위가 해당 배열 안쪽의 범위인지!
#         if 0 <= ci < N: # and 0 <= cj < N:
#             print(arr[ci][cj])
#         # 하 (i+1, j)
#         ci, cj = i + 1, j
#         if 0 <= ci < N:
#             print(arr[ci][cj])
#         # 좌 (i  , j-1)
#         ci, cj = i, j - 1
#         if 0 <= cj < N:
#             print(arr[ci][cj])
#         # 우 (i  , j+1)
#         ci, cj = i, j + 1
#         if 0 <= cj < N:
#             print(arr[ci][cj])

# arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# N = 3
# # 열 우선 순회
# for i in range(N):
#     for j in range(N):
#         # print(arr[i][j])
#         # 상 (i-1,j)
#         # 하 (i+1,j)
#         # 좌 (i,j-1)
#         # 우 (i,j+1)
#         for ci,cj in [(i - 1, j),(i + 1, j),(i, j - 1),(i, j + 1)]:
#         # 범위가 해당 배열 안쪽의 범위인지!
#             if 0 <= ci < N and 0 <= cj < N:
#                 print(arr[ci][cj])

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
N = 3

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
# 델타 탐색 1. 범위를 배열 안쪽인지를 검사

for i in range(N):
    for j in range(N):
        for k in range(4):
            ci, cj = i + di[k], j + di[k]
            # 범위가 해당 배열 안쪽의 범위인지!
            if 0 <= ci < N and 0 <= cj < N:
                print(arr[ci][cj])
# 델타 탐색 2. 범위가 배열 바깥인 경우를 제외
for i in range(N):
    for j in range(N):
        for k in range(4):
            ci, cj = i + di[k], j + di[k]
            # 범위가 해당 배열 안쪽의 범위인지!
            if 0 > ci or ci >= N or 0 > cj or cj > N:
                continue
        print(arr[ci][cj])
