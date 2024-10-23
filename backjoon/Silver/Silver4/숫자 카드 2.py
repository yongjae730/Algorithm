N = int(input())
arr = sorted(list(map(int, input().split())))
M = int(input())
target_lst = list(map(int, input().split()))
result = [0 for _ in range(M)]

for target in target_lst:
    # lower bound 찾기
    start = 0
    end = N

    while start < end:
        mid = (start + end) // 2
        if arr[mid] >= target:
            end = mid
        else:
            start = mid + 1
    lower = start

    # upper bound 찾기
    start = 0
    end = N

    while start < end:
        mid = (start + end) // 2
        if arr[mid] > target:
            end = mid
        else:
            start = mid + 1
    upper = start

    # 결과 계산
    result.append(upper - lower)

print(*result)