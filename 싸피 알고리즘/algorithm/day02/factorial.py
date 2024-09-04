# # 팩토리얼 함수
# def factorial(x):
#     # 종료조건 : x 의 값이 1이 되었을 때
#     if x == 1:
#         return 1
#
#     # 재귀호출
#     result = x * factorial(x - 1)
#     return result
#
# result = factorial(4)
# print(result)

# 피보나치 함수
# fibo(x) = fibo(x-1) + fibo(x-2)
def fibo(x):
    # 종료조건
    if x < 2:
        return x

    # 재귀호출
    result = fibo(x-1) + fibo(x-2)
    return result













