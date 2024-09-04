import sys

sys.stdin = open('input.txt')

# 입력
for _ in range(10):
    # 테스트 케이스 번호
    tc = int(input())
    # 100x100 이차원 배열 arr
    arr = [list(map(int, input().split())) for _ in range(100)]
    # 로직
    mx_total = 0  # 합에 되한 최대값
    # 가로를 먼저 순회
    for i in range(100):
        total = 0  # 가로에 있는 한 줄에 대한 값을 모두 누적 시키는 변수
        for j in range(100):
            total += arr[i][j]
        # 한 행의 합과 현재 최대값과 비교하여 갱신
        mx_total = max(total, mx_total)
    # 전치행렬 만들기(90도 뒤집기) 세로를 할 필요가 없다.
    arr = list(map(list, zip(*arr)))  # ->
    for i in range(100):  # 전치행렬을 했기에 가로와 같지만 실제로는 세로를 했음.
        total = 0
        for j in range(100):
            total += arr[i][j]
        mx_total = max(total, mx_total)

    # # 세로를 순회
    # for j in range(100):
    #     total = 0  # 세로에 있는 한 줄에 대한 값을 모두 누적 시키는 변수
    #     for i in range(100):s
    #         total += arr[i][j]  # total += arr[j][i]도 가능
    #         # 한 열의 합과 현재 최대값과 비교하여 갱신
    #     mx_total = max(total, mx_total)

    # 대각선 정방향
    # for i in range(100):
    #     for j in range(100):
    #         if i == j:
    #             total += arr[i][j]
    total = 0
    for i in range(100):
        total += arr[i][i]
    mx_total = max(total, mx_total)

    # 대각선 역방향
    total = 0
    for i in range(100):
        total += arr[i][100 - i - 1]
    mx_total = max(total, mx_total)
    # 출력
    print(f'#{tc} {mx_total}')
