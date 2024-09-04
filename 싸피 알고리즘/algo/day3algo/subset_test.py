# 부분 집합 만들기
arr = [1, 2, 3, 4, 5, 6]
N = len(arr)
# 부분 집합을 만들 수 있는 경우의 수를 모두 순회 : 2 ** N
for i in range(1 << N):  # i : 0~(2 ** N -1)
    # 해당 집합의 요소를 누적하기 위한 total
    subset = []
    # 해당의 부분집합에 어떤 원소가 포함되는지 유무확인
    for j in range(N):
        if i & (1 << j):  # j 번째에 있는 비트가 1인지를 확인!
            subset.append(arr[j])
    print(subset)
