# 입력
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    # 로직 (이차원 배열, 값 대입으로 진행)
    pascal = [[0] * N for _ in range(N)]

    # 1. 첫번째 세로 줄을 1값을 할당.
    for i in range(N):
        pascal[i][0] = 1
    # 2. 정 대각선의 줄에 1값을 할당.
    for i in range(N):
        pascal[i][i] = 1
    # 3. 파스칼 삼각형의 '안쪽 데이터' 계산하고 할당
    # (i,j)좌표의 값을 구한다면...
    # (i-1,j-1)좌표값 + (i-1,j)좌표값
    for i in range(2, N):
        for j in range(1, i):
            pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
    # 출력
    # print(f'#{tc}')
    # for i in range(N):
    #     for j in range(N):
    #         if pascal[i][j] != 0:
    #             print(pascal[i][j], end=' ')
    #     print()
    # print(f'#{tc}')
    # for i in range(N):
    #     for j in range(N):
    #         if j>i:
    #             break
    #         print(pascal[i][j], end=' ')
    #     print()
    print(f'#{tc}')
    for i in range(N):
        print(*pascal[i][:i+1])