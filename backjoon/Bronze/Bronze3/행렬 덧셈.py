import sys

n,m = map(int,input().split())

lst_a = []
lst_b = []

for i in range(n):
    lst_c = list(map(int,sys.stdin.readline().split()))
    lst_a.extend([lst_c])

for j in range(n):
    lst_d = list(map(int,sys.stdin.readline().split()))
    lst_b.extend([lst_d])

for k in range(n):
    for l in range(m):
        lst_a[k][l] +=lst_b[k][l]


for _ in range(len(lst_a)):
    # [[4, 4, 4],
    #  [6, 6, 6],
    #  [5, 6, 100]]
    for q in range(len(lst_a[_])):
        print(lst_a[_][q], end = ' ')
    print()
