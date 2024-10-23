import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

cnt = 0
for i in range(len(arr)):
    s = 0
    e = len(arr) - 1
    while s < e:
        if arr[s]+arr[e] == arr[i]:
                if s == i:
                    s += 1
                elif e ==i:
                    e -=1
                else:
                    cnt += 1
                    break
        elif arr[s]+arr[e] > arr[i]:
            e -= 1
        elif arr[s]+arr[e] < arr[i]:
            s += 1



print(cnt)
