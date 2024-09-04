# 바이너리 서치 구현
# [시작점, 끝점] 영역을 절반씩 줄여가면서 탐색
def binarySearch(arr, N, target):
    # 시작점 끝점
    start = 0
    end = N - 1
    # 시작점과 끝점이 서로 교차할 때 까지 반복
    while start <= end:
        # 중간값
        middle = (start + end) // 2
        # 내가 원하는 값을 찾는 경우
        if arr[middle] == target:
            return middle  # return True

        # 찾지 못하는 경우 (UP/DOWN) 범위 절반 줄인다
        elif arr[middle] > target:
            end = middle - 1
        else:
            start = middle + 1
    return -1


arr = list(range(100))
result = binarySearch(arr, len(arr), 60)
print(result)
