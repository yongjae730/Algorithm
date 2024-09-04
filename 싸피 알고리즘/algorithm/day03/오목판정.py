# import sys
#
# sys.stdin = open("sample_input.txt")
#
# # 델타탐색...
# # => (x, y) 특정좌표를 기준으로 해서
# #    다른 상대좌표를 탐색하는 방법...
# # 해당 델타 배열이 없어도
# # 상대 좌표를 탐색하는 것이라면 ->
# # 그것이 델타 탐색이다!!
# # di = [1, 0, -1, 0]
# # dj = [0, 1, 0, -1]
#
# # 입력
# # [입력]
# # 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# T = int(input())
# for tc in range(1, T + 1):
#     # 각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(5 ≤ N ≤ 20)이 주어진다.
#     N = int(input())
#     # 다음 N개의 줄의 각 줄에는 길이 N인 문자열이 주어진다. 각 문자는 ‘o’또는 ‘.’으로, ‘o’는 돌이 있는 칸을 의미하고, ‘.’는 돌이 없는 칸을 의미한다.
#     boards = [list(input()) for _ in range(N)]
#
#     # 로직 (바둑판 내의 오목 검사...!)
#     # 모든 좌표(i,j) 다 탐색하면서...???
#     #           -> i, j 좌표 인접해 있는 오목이 있나...
#     result = "NO"
#     for i in range(N):
#         for j in range(N):
#             # (i, j) 좌표를 기준으로 하여 오목이 8방향 내에 존재하는지!
#             # ->
#             if boards[i][j] == 'o' and j + 4 < N \
#                     and boards[i][j + 1] == 'o' \
#                     and boards[i][j + 2] == 'o' \
#                     and boards[i][j + 3] == 'o' \
#                     and boards[i][j + 4] == 'o':
#                 result = "YES"
#             # <-
#             elif boards[i][j] == 'o' and 0 <= j - 4 < N \
#                     and boards[i][j - 1] == 'o' \
#                     and boards[i][j - 2] == 'o' \
#                     and boards[i][j - 3] == 'o' \
#                     and boards[i][j - 4] == 'o':
#                 result = "YES"
#             # 위
#             elif boards[i][j] == 'o' and 0 <= i - 4 < N \
#                     and boards[i - 1][j] == 'o' \
#                     and boards[i - 2][j] == 'o' \
#                     and boards[i - 3][j] == 'o' \
#                     and boards[i - 4][j] == 'o':
#                 result = "YES"
#
#             # 아래
#             elif boards[i][j] == 'o' and i + 4 < N \
#                     and boards[i + 1][j] == 'o' \
#                     and boards[i + 2][j] == 'o' \
#                     and boards[i + 3][j] == 'o' \
#                     and boards[i + 4][j] == 'o':
#                 result = "YES"
#
#             # 정대각선
#             elif boards[i][j] == 'o' and i + 4 < N and j + 4 < N \
#                     and boards[i + 1][j + 1] == 'o' \
#                     and boards[i + 2][j + 2] == 'o' \
#                     and boards[i + 3][j + 3] == 'o' \
#                     and boards[i + 4][j + 4] == 'o':
#                 result = "YES"
#
#             # 정대각선(역)
#             elif boards[i][j] == 'o' and 0 <= i - 4 and 0 <= j - 4 \
#                     and boards[i - 1][j - 1] == 'o' \
#                     and boards[i - 2][j - 2] == 'o' \
#                     and boards[i - 3][j - 3] == 'o' \
#                     and boards[i - 4][j - 4] == 'o':
#                 result = "YES"
#
#             # 역대각선
#             elif boards[i][j] == 'o' and i - 4 >= 0 and j + 4 < N \
#                     and boards[i - 1][j + 1] == 'o' \
#                     and boards[i - 2][j + 2] == 'o' \
#                     and boards[i - 3][j + 3] == 'o' \
#                     and boards[i - 4][j + 4] == 'o':
#                 result = "YES"
#
#             # 역대각선(역)
#             elif boards[i][j] == 'o' and i + 4 < N and j - 4 >= 0 \
#                     and boards[i + 1][j - 1] == 'o' \
#                     and boards[i + 2][j - 2] == 'o' \
#                     and boards[i + 3][j - 3] == 'o' \
#                     and boards[i + 4][j - 4] == 'o':
#                 result = "YES"
#
#     # 출력
#     print(f"#{tc} {result}")
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    boards = [list(input()) for _ in range(N)]
    result = "NO"
    for i in range(N):
        for j in range(N):
            # (i, j) 좌표를 기준으로 하여 오목이 8방향 내에 존재하는지!
            # ->
            # if boards[i][j] == 'o' and j + 4 < N \
            #         and boards[i][j + 1] == 'o' \
            #         and boards[i][j + 2] == 'o' \
            #         and boards[i][j + 3] == 'o' \
            #         and boards[i][j + 4] == 'o':
            #     result = "YES"
            cnt = 0  # 카운트 배열 (돌의 갯수 카운트)
            for k in range(5):
                if 0 <= i < N and 0 <= j + k < N and boards[i][j + k] == 'o':
                    cnt += 1
            if cnt == 5:
                result = "YES"
            # 아래
            # elif boards[i][j] == 'o' and i + 4 < N \
            #         and boards[i + 1][j] == 'o' \
            #         and boards[i + 2][j] == 'o' \
            #         and boards[i + 3][j] == 'o' \
            #         and boards[i + 4][j] == 'o':
            #     result = "YES"
            cnt = 0  # 카운트 배열 (돌의 갯수 카운트)
            for k in range(5):
                if 0 <= i + k < N and 0 <= j < N and boards[i + k][j] == 'o':
                    cnt += 1
            if cnt == 5:
                result = "YES"
            # 정대각선
            # elif boards[i][j] == 'o' and i + 4 < N and j + 4 < N \
            #         and boards[i + 1][j + 1] == 'o' \
            #         and boards[i + 2][j + 2] == 'o' \
            #         and boards[i + 3][j + 3] == 'o' \
            #         and boards[i + 4][j + 4] == 'o':
            #     result = "YES"
            cnt = 0  # 카운트 배열 (돌의 갯수 카운트)
            for k in range(5):
                if 0 <= i + k < N and 0 <= j + k < N and boards[i + k][j + k] == 'o':
                    cnt += 1
            if cnt == 5:
                result = "YES"

            # 역대각선
            # elif boards[i][j] == 'o' and i - 4 >= 0 and j + 4 < N \
            #         and boards[i - 1][j + 1] == 'o' \
            #         and boards[i - 2][j + 2] == 'o' \
            #         and boards[i - 3][j + 3] == 'o' \
            #         and boards[i - 4][j + 4] == 'o':
            #     result = "YES"
            cnt = 0  # 카운트 배열 (돌의 갯수 카운트)
            for k in range(5):
                if 0 <= i - k < N and 0 <= j + k < N and boards[i - k][j + k] == 'o':
                    cnt += 1
            if cnt == 5:
                result = "YES"

    # 출력
    print(f"#{tc} {result}")
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    boards = [list(input()) for _ in range(N)]
    result = "NO"
    for i in range(N):
        for j in range(N):
            # ->
            # cnt = 0 # 카운트 배열 (돌의 갯수 카운트)
            # for k in range(5):
            #     if 0 <= i < N and 0 <= j + k < N and boards[i][j+k] == 'o':
            #         cnt += 1
            # if cnt == 5:
            #     result = "YES"
            # # 아래
            # cnt = 0
            # for k in range(5):
            #     if 0 <= i + k < N and 0 <= j < N and boards[i+k][j] == 'o':
            #         cnt += 1
            # if cnt == 5:
            #     result = "YES"
            # # 정대각선
            # cnt = 0
            # for k in range(5):
            #     if 0 <= i + k < N and 0 <= j + k < N and boards[i+k][j + k] == 'o':
            #         cnt += 1
            # if cnt == 5:
            #     result = "YES"
            #
            # cnt = 0
            di = [0, 1, 1, -1]
            dj = [1, 0, 1, 1]
            for l in range(4):
                cnt = 0
                for k in range(5):
                    if 0 <= i + (k * di[l]) < N \
                            and 0 <= j + (k * dj[l]) < N \
                            and boards[i + (k * di[l])][j + (k * dj[l])] == 'o':
                        cnt += 1
                if cnt == 5:
                    result = "YES"

    # 출력
    print(f"#{tc} {result}")
