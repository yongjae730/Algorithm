n,m = map(int, input().split())
basket = [0]*n
temp = n+1

for a in range(n):
    basket[a] = a+1

for b in range(m):
    i,j = map(int, input().split())
    temp = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = temp

for c in range(n):
    print(basket[c], end=" ")