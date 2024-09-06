# 병합 정렬 : 분할 정복 기법에 의한 정렬 알고리즘
def merge_sort(arr):
    def merge(arr, left_arr, right_arr):
        i = j = k = 0

        # 왼쪽 배열과 오른쪽 배열의 모든 원소를 merged_arr에 추가
        while i < len(left_arr) and j < len(right_arr):
            # 왼쪽 배열의 i 인덱스 요소와 오른쪽 배열의 j 인덱스 요소를 비교
            # 더 작은 교소를 merged_arr에 추가
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
                k += 1
            else:
                arr[k] = right_arr[j]
                j += 1
                k += 1
        if i < len(left_arr):
            arr[k:] = left_arr[i:]
        else:
            arr[k:] = right_arr[j:]

        return arr

    # 기저조건
    if len(arr) == 1:
        return arr
    # 분할(divide) : 요소를 절반씩 나눈다.
    mid = len(arr) // 2
    left_arr = arr[:mid]  # 왼쪽 배열
    right_arr = arr[mid:]  # 오른쪽 배열

    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)
    # 정복(병합)하도록 병합 과정
    return merge(arr, left_arr, right_arr)


arr = [5, 2, 4, 7, 1, 4, 9]
sorted_arr = merge_sort(arr)
print(sorted_arr)
