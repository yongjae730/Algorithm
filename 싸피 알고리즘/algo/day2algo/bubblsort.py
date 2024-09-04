def bubble_sort(lst):
    # 요소 N의 갯수
    N = len(lst)
    # i : N-1 -> 1 , 마지막 범위
    for i in range(N-1, 0 , -1):
        # j : [0:i), 0<= j < i
        for j in range(0, i):
            # 인접한 요소를 비교 후 교환
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]


arr = [ 9, 8, 7, 6, 5, 4, 3, 2, 1 ]
bubble_sort(arr)
print(arr)