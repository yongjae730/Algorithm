# # 1. 피보나치 수열의 재귀함수
# def fibo(n):
#     # 기저조건
#     if n < 2:
#         return n
#     # 재귀호출
#     result = fibo(n - 1) + fibo(n - 2)
#     return result


# N_MAXIMUM = 1000
#
# # 메모를 할 리스트를 만들기
# # 입력값인 n에 대해서 피보나치 수열의 결과를 저장하는 역할
# # memo[n] = n번째 피보나치 결과값...
# # *주의 : n은 0 ~ 1000까지만 가능!
# memo = [0] * (N_MAXIMUM + 1)
#
# # 2. 피보나치 수열의 메모이제이션
# def fibo(n):
#     # 기저조건
#     if n < 2:
#         return n
#     # 최적화 (메모이제이션 배열 활용)
#     # 이미 메모가 진행되어 있던 값이었다면! 그 값을 활용!
#     if memo[n] != 0:
#         return memo[n]
#     # 재귀호출
#     result = fibo(n - 1) + fibo(n - 2)
#     # 피보나치 결과값을 메모에 저장
#     memo[n] = result
#     return result


# fibo(10)  # O(2 ** n) -> O(n) 메모이제이션 개선!



# DP : 동적 계획법을 사용하여 작은 문제부터 큰 문제인 N까지 차근차근 푼다
dp = [0] * 1001
# fibo(0) => fibo(1) => 1
dp[0] = 0
dp[1] = 1
# fibo(n) = fibo(n-1) + fibo(n-2) 배열로서 바꾼다
# 이 과정을 아래서부터(작은문제서) 위로(큰 문제) 순차적으로 진행
for x in range(2, 1001):
    dp[x] = dp[x - 1] + dp[x - 2]
def fibo(n):
    return dp[n]

print(fibo(10))
print(fibo(100))
print(fibo(1000))

