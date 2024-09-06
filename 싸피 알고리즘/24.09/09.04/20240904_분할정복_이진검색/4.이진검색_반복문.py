arr = [2, 4, 7, 9, 11, 19, 23]


# 이진 탐색은 정렬된 데이터에 적용 가능하다.
# arr.sort()


def binary_search(target):
    low = 0
    high = len(arr) - 1
    # 탐색 횟수 카운팅
    cnt = 0

    while low <= high:
        mid = (low + high) // 2  # 중앙값을 지정해 준다.
        cnt += 1

        if arr[mid] == target:  # 타겟을 발견했다면 끝내고
            return mid, cnt
        elif arr[mid] > target:  # 타겟을 발견 못했다면 (가운데가 키보다 더 크다면)
            high = mid - 1  # 왼쪽(작은수로 정렬 된곳)을 보면 되니까 mid-1을 high로 바꾼다.
        else:  # 반대로 타겟을 발견 못했고, 가운데가 키보다 더 작다면
            low = mid + 1  # 오른쪽을 보면 되니까 mid+1를 low로 바꾼다.
    return -1, cnt


print(f'9 = {binary_search(9)}')
print(f'2 = {binary_search(2)}')
print(f'20 = {binary_search(20)}')
