N = int(input())

num_lst = []
for i in range(1, N + 1):
    num_lst.append(str(i))

for num in num_lst:

    cnt = 0
    for n in num:
        if n == '3'or n == '6' or n == '9':
            cnt += 1
    if cnt != 0:
        print('-' * cnt, end=' ')
    else:
        print(num, end=' ')
