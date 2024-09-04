def bubble_sort(lst):
    N = len(lst)
    for i in range(N - 1, 0, -1):
        for j in range(0, i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


arr = [9, 8, 7, 6, 5, 4, 3,  2, 1]
bubble_sort(arr)
print(arr)
