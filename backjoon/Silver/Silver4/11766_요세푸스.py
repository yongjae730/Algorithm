N, K = map(int, input().split())

q = []
lst = []
for i in range(1, N + 1):
    q.append(i)
j = 0
while len(lst) < N:
    j = j + K - 1
    if j >= len(q):
        j = j % len(q)

    lst.append(q[j])

    q.pop(j)

print('<', end ='')

for i in range(len(lst)):
    if i != len(lst)-1:
        print(f'{lst[i]}, ', end = '')
    else:
        print(f'{lst[i]}'+'>')

