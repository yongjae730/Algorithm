n, m = map(int, input().split())

bucket = [0] * (n+1)
for _ in range(1,m+1):
    i, j, k = map(int,input().split())
    for a in range(i,j+1):
        bucket[a] = k


for i in range(1, n+1):
    print(bucket[i], end = ' ') 