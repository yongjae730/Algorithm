# 점화식 : f(x) = f(x-10) + 2*f(x-20)
# 1. 재귀함수로 작성하였을 때...
# 시간 복잡도 O(2**n)
# def f(x):
#     # 기저조건(종료 조건) : ???
#     if x == 10:
#         return 1
#     elif x == 20:
#         return 3
#     # 재귀호출
#     result = f(x - 10) + 2 * f(x - 20)
#     return result
# 2. Memoization
# 시간복잡도 O(n)
# memo = [0]*301 # 메모 배열
# def f(x):
#     # 기저조건(종료 조건) : ???
#     if x == 10:
#         return 1
#     elif x == 20:
#         return 3
#     # 최적화 (이미 계산된 값이 있는 경우 활용!)
#     elif memo[x] != 0:
#         return memo
#     # 재귀호출
#     result = f(x - 10) + 2 * f(x - 20)
#     memo[x] = result
#     return
# 3.DP
dp = [0] * 301  # 메모 배열
dp[10] = 1
dp[20] = 3
# bottom- up 접근 ... 차근차근...(점화식)
for x in range(30, 301, 10):
    dp[x] = dp[x - 10] + 2 * dp[x - 20]
# 입력
# 첫 줄에 테스트 케이스 개수 T가 주어진다.
T = int(input())
for tc in range(1, T + 1):
    # 다음 줄 부터 테스트 케이스 별로 N이 주어진다.
    # 종이를 붙이는 교실의 가로 길이
    N = int(input())
    # 로직
    result = dp[N]

    # 출력
    print(f'#{tc} {result}')
