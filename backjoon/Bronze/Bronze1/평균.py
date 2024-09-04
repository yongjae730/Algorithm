n = int(input())
s = list(map(int, input().split()))
m = max(s)

for i in range(n):
    # range(1,n+1)은 왜안되는거지?
    s[i] = s[i]/m*100

print(sum(s)/n)