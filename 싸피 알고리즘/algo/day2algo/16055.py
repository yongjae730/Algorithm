'''
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175
'''

# T = int(input()) #테스트 케이스 갯수
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     #가장 큰 값
#     max_v = arr[0]
#     for i in range(1, N):
#         if max_v < arr[i]:
#             max_v = arr[i]
#     min_v = arr[0]
#     for i in range(1, N):
#         if min_v > arr[i]:
#             min_v = arr[i]
#
#     print(f'#{tc}{max_v-min_v}')



# 테스트 케이스 T
T = int(input().strip())
# 테스트 케이스 수 만큼 순회
for tc in range(1, T+1):
    # 입력
    # 각 케이스의 첫 줄에 양수의 개수 N이 주어진다. (5 ≤ N ≤ 1000)
    N = int(input())
    # 다음 줄에 N 개의 양수 Ai가 주어진다 (1 ≤ ai ≤ 1000000)
    arr = list(map(int,input().split()))
    # 로직
    # 가장 큰 수
    # mx = max(arr)
    mx = arr[0]
    for i in range(1,N):
        if mx < arr[i]:
            mx = arr[i]
    # 가장 작은 수
    mn = arr[0]
    for i in range(1, N):
        if mn > arr[i]:
            mn = arr[i]

    result = mx -mn
    #출력
    print(f'#{tc} {result}')