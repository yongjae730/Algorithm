N = int(input())
arr = sorted(list(map(int, input().split())))
M = int(input())
target_lst = list(map(int, input().split()))
result = [0 for _ in range(M)]
#
# for i in range(len(target_lst)):
#
#     target = target_lst[i]
#     start = 0
#     end = len(arr) - 1
#     upper = 0
#     lower = 0
#     # upper
#     while start <= end :
#
#         mid = (start + end) // 2
#         if arr[mid] == target:
#             upper = mid
#             start = mid + 1
#         if arr[mid] > target:
#             end = mid
#         elif arr[mid] < target:
#             start = mid + 1
#     if arr[start] == target:
#         upper = start
#
#     start = 0
#     end = len(arr) - 1
#
#     # lower
#     while start < end:
#
#         mid = (start + end) // 2
#
#         if arr[mid] == target:
#             lower = mid
#             end = mid
#
#         if arr[mid] > target:
#             end = mid
#
#         elif arr[mid] < target:
#             start = mid + 1
#     if arr[end] == target:
#         lower = end
#
#     if lower == 0 and upper == 0:
#         result[i] = 0
#     else:
#         result[i] = upper - lower + 1
#
# print(*result)
####################################
# count_arr = [0] * 20000001
#
# for i in arr:
#     num = i + 10000000
#     count_arr[num] += 1
# for j in range(len(target_lst)):
#     result[j] += count_arr[target_lst[j]+10000000]
###########################################
for target in target_lst:
    # lower bound 찾기
    start = 0
    end = N

    while start < end:
        mid = (start + end) // 2
        if arr[mid] >= target:
            end = mid
        else:
            start = mid + 1
    lower = start

    # upper bound 찾기
    start = 0
    end = N

    while start < end:
        mid = (start + end) // 2
        if arr[mid] > target:
            end = mid
        else:
            start = mid + 1
    upper = start

    # 결과 계산
    result.append(upper - lower)

print(*result)