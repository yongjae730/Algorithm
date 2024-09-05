def merge_sort(arr):
    if len(arr) == 1:
        return arr

    left = arr[:len(arr) // 2]
    right = arr[len(arr) // 2:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    global cnt
    result = [0] * (len(left) + len(right))
    l = r = 0
    if left[-1] > right[-1]:
        cnt += 1


    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l + r] = left[l]
            l += 1
        else:
            result[l + r] = right[r]
            r += 1
    while l < len(left):
        result[l + r] = left[l]
        l += 1
    while r < len(right):
        result[l + r] = right[r]
        r += 1
    return result


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    result = merge_sort(arr)
    print(f'#{tc} {result[N//2]} {cnt}')
