def counting_sort(lst):
    N = len(lst)
    M = max(lst)
    counts = [0] * (M + 1)

    for i in lst:
        counts[i] += 1

    for j in range(1, M + 1):
        counts[j] = counts[j] + counts[j - 1]

    temp = [0] * N
    for k in range(N - 1, -1, -1):
        x = lst[k]
        counts[x] -= 1
        temp[counts[x]] = x

    return temp


arr = [4, 5, 9, 0, 7, 1, 3, 2, 6, 8, 3, 5, 7, 6, 1, 6, 8]
result = counting_sort(arr)
print(*result)
