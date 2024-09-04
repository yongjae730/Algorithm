N = 8
for tc in range(1, 11):
    # 각 테스트 케이스의 첫 번째 줄에는 찾아야 하는 회문의 길이
    M = int(input())
    # 주어지며, 다음 줄에 8x8 크기의 글자판이 주어진다.
    boards = [list(input()) for _ in range(8)]
    # 로직 ( 가로와 세로에 길이가 M만큼 되어 있는 회문을 찾는다.)
    cnt = 0  # 회문의 갯수를 카운트 할 변수 cnt
    # 가로 우선 순회
    for i in range(N):
        for j in range(N - M + 1):
            # 길이가 M 만큼의 요소가 회문인지 확인!
            # [j, j+M) 범위 -> 회문 유무!
            if boards[i][j:j + M] == boards[i][j:j + M][::-1]:
                cnt += 1
    # 전치행렬 행 <-> 열을 뒤바꾸기
    boards = list(map(list, zip(*boards)))

    # 가로로 다시 순회
    for i in range(N):
        for j in range(N - M + 1):
            # 길이가 M 만큼의 요소가 회문인지 확인!
            # [j, j+M] 범위 -> 회문 유무!
            if boards[i][j:j + M] == boards[i][j:j + M][::-1]:
                cnt += 1

    # 출력
    print(f'#{tc} {cnt}')

# T = 10
# 입력
"""
4
CBBCBAAB
CCCBABCB
CAAAACAB
BACCCCAC
AABCBBAC
ACAACABC
BCCBAABC
ABBBCCAA
"""

#
#
#
# def palindrome_check(boards, M, i, j):
#     is_palindrome = True
#     for k in range(M // 2):
#         if boards[j + k][i] == boards[j + M - k][i]:
#             continue
#         else:  # 회문이 아니라면 False!
#             is_palindrome = False
#             break
#     # 만약에 회문이라면 카운트 값을 1 증가
#     return is_palindrome
#
# # 격차판의 한변의 길이
# N = 8
# for tc in range(1, T + 1):
#     # 각 테스트 케이스의 첫 번째 줄에는 찾아야 하는 회문의 길이가
#     M = int(input())
#
#     # 주어지며, 다음 줄에 8x8 크기의 글자판이 주어진다.
#     boards = [list(input()) for _ in range(N)]
#
#     # 로직 (가로와 세로에 길이가 M만큼 되어있는 회문을 찾는다!)
#     # 회문의 갯수를 카운트 할 변수 cnt
#     cnt = 0
#     # 가로 우선 순회
#     for i in range(N):
#         for j in range(N - M + 1):  # [0, N-M]
#             # 길이가 M 만큼의 요소가 회문인지 확인!
#             # [j, j+M] 범위 -> 회문 유무!
#             is_palindrome = True
#             for k in range(M // 2):
#                 if boards[i][j + k] == boards[i][j + M - k]:
#                     continue
#                 else:  # 회문이 아니라면 False!
#                     is_palindrome = False
#                     break
#             # 만약에 회문이라면 카운트 값을 1 증가
#             if is_palindrome == True:
#                 cnt += 1
#     # 세로 우선 순회
#     for j in range(N):
#         for i in range(N - M + 1):  # [0, N-M]
#             # 길이가 M 만큼의 요소가 회문인지 확인!
#             # [j, j+M] 범위 -> 회문 유무!
#             is_palindrome = palindrome_check(boards, M, i, j)
#             if is_palindrome == True:
#                 cnt += 1
#     # 출력
#     print(f"#{tc} {cnt}")
