N, M = map(int,input().split())

arr = list(i+1 for i in range(N))

for _ in range(M):
    i,j = map(int,input().split())
    for k in range(((j-i)//2)+1):
        arr[i+k-1], arr[j-k-1] = arr[j-k-1], arr[i+k-1]

print(*arr)
