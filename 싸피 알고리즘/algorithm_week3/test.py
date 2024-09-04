# ### 삼성시의 버스 노선
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())  # 노선 수
#
#     cnt = [0] * 5001  # 5000번 정류장 까지
#     for _ in range(N):
#         A, B = map(int, input().split())
#         for i in range(A, B + 1):
#             cnt[i] += 1
#
#     P = int(input())
#     bus_stop = [int(input()) for _ in range(P)]
#     print(f'#{tc}', end=' ')
#     for j in bus_stop:
#         print(cnt[j], end=' ')
#     print()
# #####################################################
# ### 풍선팡
#
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     max_v = 0
#     for i in range(N):
#         for j in range(M):
#             cnt = arr[i][j]
#             for k in range(4):
#                 for l in range(1, arr[i][j] + 1):
#                     ni = i + di[k] * l
#                     nj = j + dj[k] * l
#                     if 0 <= ni < N and 0 <= nj < M:
#                         cnt += arr[ni][nj]
#             if cnt > max_v:
#                 max_v = cnt
#     print(f'#{tc} {max_v}')
# ##########################################################
# ## 오셀로
#
# def f(i, j, bw, N):
#     board[i][j] = bw  # 지정된 돌 놓기
#
#     for di, dj in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
#         ni, nj = i + di, j + dj
#         tmp = []  # 뒤집을 돌의 인덱스를 저장
#         while 0 <= ni < N and 0 <= nj < N and board[ni][nj] == op[bw]:  # 반대색 돌이면
#             tmp.append((ni, nj))  # 뒤집을 돌을 저장하고
#             ni, nj = ni + di, nj + dj  # 현재 방향으로 계속 이동
#         if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == bw:
#             for p, q in tmp:
#                 board[p][q] = bw
#
#
# B = 1
# W = 2
# op = [0, 2, 1]
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())  # 보드의 한 변의 길이 N 놓을 놓는 횟수 M
#     play = [list(map(int, input().split())) for _ in range(M)]
#
#     board = [[0] * N for _ in range(N)]
#     # 중심부 돌 배치
#     board[N // 2 - 1][N // 2 - 1] = W
#     board[N // 2 - 1][N // 2] = B
#     board[N // 2][N // 2 - 1] = B
#     board[N // 2][N // 2] = W
#
#     # 돌 놓기
#     for col, row, bw in play:  # 입력순서 주의, col, row는 1부터 시작 board는 0부터 시작
#         f(row - 1, col - 1, bw, N)  # 돌 놓기, 뒤집기
#
#     bcnt = wcnt = 0  # 검은돌 갯수, 흰 돌 개수
#
#     for i in range(N):
#         for j in range(N):
#             if board[i][j] == B:
#                 bcnt += 1
#             elif board[i][j] == W:
#                 wcnt += 1
#     print(f'#{tc} {bcnt} {wcnt}')
