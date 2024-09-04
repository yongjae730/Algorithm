def power(N,M):
    if M == 0:
        return 1

    return N*power(N,M-1)

for tc in range(1,11):
    T = int(input())
    N,M = map(int, input().split())

    power(N,M)

    print(f'#{tc} {power(N,M)}')
#-----------#
# 강사님 코드
# 복잡해 보이지만 시간복잡도 측면에서 엄청난 이득이다.
# 시간복잡도 : O(m) -> O(log(m))
# 테스트케이스 수 T
T = 10
#
for _ in range(1, T + 1):
    # 입력
    # 각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가
    tc = int(input())
    # 그 다음 줄에는 두 개의 숫자가 주어진다.
    N, M = map(int, input().split())  # [9, 8]


    # 로직
    # 재귀호출을 위한 거듭제곱 함수
    # 시간복잡도 : O(m)
    def my_pow(n, m):  # n ** 0
        # 기저조건 : m이 0일 때...
        if m == 0:
            return 1
        # 재귀호출
        if m % 2 == 0: # M 짝수
            result = my_pow(n * n, m // 2)
        else: # M 홀수
            result = n * my_pow(n * n, m // 2)
        return result

    result = my_pow(N, M)

    # 출력
    print(f"#{tc} {result}")
