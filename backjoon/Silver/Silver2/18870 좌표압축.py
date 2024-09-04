import sys
n = int(input())
arr = list(map(int,sys.stdin.readline().split()))

arr2 = sorted(list(set(arr)))

dic = {}

for j in range(len(arr2)):
    dic[arr2[j]] = j

for i in arr:
    print(dic[i], end = ' ')