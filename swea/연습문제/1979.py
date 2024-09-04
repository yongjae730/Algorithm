import sys

sys.stdin = open('../input/1979.txt')

# T = int(input())
# for tc in range(1, T + 1):
#     N, K = map(int, input().split())
#     puzzle = []
#     cnt = 0
#     for i in range(N):
#         cell = list(map(int, input().split()))
#         puzzle.append(cell)
#         # 가로 혹은 세로로 탐색 얼만큼? K만큼의 길이를
#         # x 혹은 y 는 그대로 두고 < range = 1
#         # k만큼의 길이? -> 5줄(index = 4)이면 2번 인덱스까지 가능
#         # N - K +1 까지
#         for y in range(N):
#             for x in range(N):
#
#                 for k in range(1):
#                     for l in range(N - K + 1):
#
#
#     print(puzzle)

# 연속된 1을 찾는방법 -> 111을 찾아도 1111이 나와도 거르지 못함
# 1을 만날 때 마다 cnt를 늘린다, 0 을만나면 break  cnt가 3이되면 찾는다 -> 이방법도 cnt가 4가 되어도 그냥 횟수를 세어버림
# -> if 조건이 너무 많이 붙는데 예외상황을 모두 찾기 힘듬
# 문자열 '111'을 찾아서 비교? -> 이차원 배열의 탐색(오늘 배운거)와는 관계가 없음..
# 주어진 K+1까지 탐색해서 1이 있든 0이 있든 break? -> 이전 1도 탐색해야함. 범위가 너무 넓어짐
# 범위가 넓어지는 것 까진 문제가 없으나 3개까진 1이 있어도 되고 그 이상 1이 있다면 예외 조건을 넣는 걸 구현 할 줄 모르겠음 ...ㅠ
# temp 빈 리스트 만들어서 한 줄을 받는다.


T = int(input())

for tc in range(1,T+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = 0

    for i in range(n):
        cnt = 0

        for j in range(n):
            if arr[i][j] == 1:
                cnt += 1
            if arr[i][j] == 0 or j == n - 1:
                if cnt == k:
                    result += 1
                cnt = 0

        for j in range(n):
            if arr[j][i] == 1:
                cnt += 1
            if arr[j][i] == 0 or j == n - 1:
                if cnt == k:
                    result += 1
                cnt = 0

    print(f'#{tc} {result}')