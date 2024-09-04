A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    cnt = 0
    for i in range(1 << 12):  # i : 0~(2 ** N -1)
        subset = []
        # 해당의 부분집합에 어떤 원소가 포함되는지 유무확인
        for j in range(12):
            if i & (1 << j):
                subset.append(A[j])
        if len(subset) == N:
            if sum(subset) == K:
                cnt += 1
    print(f'#{tc} {cnt}')
