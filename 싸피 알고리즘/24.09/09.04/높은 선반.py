def subset(arr, N, i):
    global difference
    global stack

    # 현재 부분 집합의 합계를 저장할 변수 초기화
    total = 0

    # 모든 요소를 고려했을 때
    if i == N:
        # 현재 부분 집합의 합계를 계산
        for k in range(N):
            if bits[k] == 1:
                total += arr[k]

                # 현재 부분 집합의 합계가 목표 B와의 차이가 최소인 경우 업데이트
                if 0 <= total - B <= difference:
                    difference = total - B
                    stack = total

        return

    # 현재 요소를 부분 집합에 포함하지 않을 경우
    bits[i] = 0
    subset(arr, N, i + 1)

    # 현재 요소를 부분 집합에 포함할 경우
    bits[i] = 1
    subset(arr, N, i + 1)


# 테스트 케이스의 수를 입력받음
T = int(input())
for tc in range(1, T + 1):
    # 요소의 수 N과 목표 값 B를 입력받음
    N, B = map(int, input().split())

    # 요소들의 리스트를 입력받음
    arr = list(map(int, input().split()))

    # 요소의 포함/미포함을 추적할 bits 리스트 초기화
    bits = [0] * N

    # 결과를 추적할 stack과 difference 초기화
    stack = 0
    difference = 999

    # subset 함수 호출하여 가장 가까운 차이를 계산
    subset(arr, N, 0)

    # 현재 테스트 케이스의 결과를 지정된 형식으로 출력
    print(f'#{tc} {difference}')
