n, m = map(int, input().split())

bucket = [0] * (n+1)
for _ in range(m):
    i, j, k = map(int,input().split())
    for a in range(i,j+1):
        bucket[a] = k

# for b in range(1):
#     print(bucket[1:n+2], end = " ")
# -> 배열이 출력됨 

for i in range(1, n+1):
    print(bucket[i], end = ' ') 
    # 한자리씩 출력
