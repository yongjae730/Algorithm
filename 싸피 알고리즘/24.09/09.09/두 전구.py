T = int(input())
total = [] # 결과들을 저장
for tc in range(1, T + 1):
    A, B, C, D = map(int, input().split())

    # 나중에 켜진 전구 시간이 시작점
    start = max(A, C)
    # 먼저 꺼진 전구 시간이 끝점
    end = min(B, D)
    result = end - start
    if result <= 0:  # 안 겹치는 경우
        result = 0
    total.append(result)

# for i in range(len(total)):
#     print(f'#{i + 1} {total[i]}')
for idx, result in enumerate(total):
    print(f'#{idx} {result}')