def binary_search(lis_helper, target):
    # 이진 탐색을 통해 target이 들어갈 위치를 찾는 함수
    left, right = 0, len(lis_helper) - 1

    while left <= right:
        mid = (left + right) // 2
        if lis_helper[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left  # target이 들어갈 위치 반환


def length_of_lis(arr):
    # lis_helper 배열은 LIS를 추적하는 배열
    lis_helper = []

    for num in arr:
        # num이 들어갈 위치를 이진 탐색으로 직접 찾음
        pos = binary_search(lis_helper, num)

        # 위치가 lis_helper의 길이와 같다면 새로운 숫자를 추가 (즉, LIS가 길어짐)
        if pos == len(lis_helper):
            lis_helper.append(num)
        else:
            # 그렇지 않다면 해당 위치 값을 num으로 갱신
            lis_helper[pos] = num

    # lis_helper 배열의 길이가 LIS의 길이
    return len(lis_helper)

N = int(input())
arr = list(map(int,input().split()))
result = length_of_lis(arr)
print(result)