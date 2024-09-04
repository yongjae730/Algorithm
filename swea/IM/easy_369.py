N = int(input())
number = []
for i in range(1, N + 1):
    number.append(str(i))

for j in number:
    cnt = 0
    for k in j:
        if k == '3' or k == '6' or k == '9':
            cnt += 1
    if cnt >0:
        print('-'*cnt, end = ' ')
    else:
        print(j, end = ' ')