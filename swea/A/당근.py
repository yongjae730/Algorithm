T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     carrots = sorted(list(map(int, input().split())))
#
#     min_v = 1000
#
#     # 같은 수는 같은 박스에 담는다.
#     for i in range(N - 2):
#         for j in range(i + 1, N - 1):
#             if carrots[i] != carrots[i + 1] and carrots[j] != carrots[j + 1]:
#                 # 1,1,1,3,3 의 경우엔 여기에 해당이 안돼
#                 # 다른 숫자 3개는 존재해야함
#                 A = i + 1  # 2+1
#                 B = j - i  #
#                 C = N - 1 - j
#
#                 if min_v > max(A, B, C) - min(A, B, C):
#                     if min_v > max(A, B, C) - min(A, B, C):
#                         min_v = max(A, B, C) - min(A, B, C)
#     if min_v == 1000:
#         min_v = -1
#     print(f'#{tc} {min_v}')

for tc in range(1, T + 1):
    N = int(input())
    carrot = list(map(int, input().split()))

    carrot.sort()
    min_v = 1000
    for i in range(N - 2):  # 소 박스의 마지막 당근
        for j in range(i + 1, N - 1):  # 중 박스의 마지막 당근
            if carrot[i] != carrot[i + 1] and carrot[j] != carrot[j + 1]:  # 같은 크기 당근이 다른 박스에 있으면 안됨
                A = i + 1  # 0 ~ i (소, 중, 대 당근의 개수 A,B,C)
                B = j - i  #
                C = N - 1 - j  # j+1 ~ N-1

                if min_v > max(A, B, C) - min(A, B, C):
                    min_v = max(A, B, C) - min(A, B, C)
    if min_v == 1000:
        min_v = -1
    print(f'#{tc} {min_v}')
