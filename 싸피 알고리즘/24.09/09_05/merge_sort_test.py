# 병합 정렬 : 분할 정복 기법에 의한 정렬 알고리즘
def merge_sort(arr):
    def merge(left_arr, right_arr):
        merged_arr = []  # 최종적으로 정렬이 완료된 배열
        i = j = 0

        # 왼쪽 배열과 오른쪽 배열의 모든 원소를 merged_arr에 추가
        while i < len(left_arr) and j < len(right_arr):
            # 왼쪽 배열의 i 인덱스 요소와 오른쪽 배열의 j 인덱스 요소를 비교
            # 더 작은 교소를 merged_arr에 추가
            if left_arr[i] < right_arr[j]:
                merged_arr.append(left_arr[i])
                i += 1
            else:
                merged_arr.append(right_arr[j])
                j += 1
        # #왼쪽에 배열 요소가 남아있는 것들을 통합
        # while i < len(left_arr):
        #     merged_arr.append(left_arr[i])
        #     i += 1
        # # 왼쪽에 배열 요소가 남아있는 것들을 통합
        # while j < len(right_arr):
        #     merged_arr.append(right_arr[j])
        #     j += 1
        # 왼쪽에 배열 요소가 남아있는 것들을 통합
        for k in range(i, len(left_arr)):
            merged_arr.append(left_arr[k])
        # 오른쪽에 배열 요소가 남아있는 것들을 통합
        for k in range(j, len(right_arr)):
            merged_arr.append(right_arr[k])
        # merged_arr += left_arr[i:]
        # merged_arr += right_arr[j:]
        return merged_arr

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
    return merge(left_arr, right_arr)


arr = [5, 2, 4, 7, 1, 4, 9]
sorted_arr = merge_sort(arr)
print(sorted_arr)