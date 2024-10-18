N = int(input())
arr = sorted(list(map(int, input().split())))
M = int(input())
target_lst = list(map(int, input().split()))
result = [0 for _ in range(M)]


for i in target_lst:
    target = i
    start = 0
    end = len(arr)-1
    cnt = 0
    while start <= end:

        mid = (start + end) //2

        if arr[mid] == target:
            pass

        elif arr[mid] > target:
            ...
        elif arr[mid] < target:
            ...
#