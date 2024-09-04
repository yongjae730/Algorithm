x = int(input())
n = int(input())

sum = 0
for i in range(1,n+1) :
    a, b = map(int, input().split())
    sum += a*b

if x == sum :
    print('Yes')
else :
    print('No')