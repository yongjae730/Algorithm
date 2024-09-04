num = input()

arr = []

for i in range(0, len(num), 7):
    arr.append(num[i:i + 7])

for j in range(len(arr)):
    result = int(arr[j], base=2)
    print(result,end = ' ')