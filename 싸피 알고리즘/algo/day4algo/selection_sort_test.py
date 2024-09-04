# 선택 정렬
def selectionSort(arr, N):
    # for i: 0 ~ n - 2
    # a[i].....a[n-1] 까지의 원소에 최소값을 찾는다.
    # a[i] <-> a[k] 요소를 교환
    for i in range(N - 1):
        mn_idx = i
        for j in range(i, N):  # for j in range(i+1,N): < mn_idx를 i로 지정했기에 이것도 가능
            # 최소값 갱신하기
            if arr[mn_idx] > arr[j]:
                mn_idx = j
        # 교환
        arr[i], arr[mn_idx] = arr[mn_idx], arr[i]


arr = [6, 2, 34, 0, 23, 21, 5, 67, 12, 54, 24, 7, 8, 4, 56]
selectionSort(arr, len(arr))
print(arr)
