N = int(input())

num_lst = []
for i in range(1, N + 1):
    num_lst.append(i)

for j in num_lst:

    num = str(j)
    cnt = 0
    for n in num:
        if n == '3' or n == '6' or n == '9':
            cnt += 1
    if cnt > 0:
        print('-' * cnt, end=' ')
    else:
        print(j, end=' ')


# for j in range(len(num_lst)):
#
#     if '3' in num_lst[j]:
#         result = num_lst[j].replace('3','-')
#         result_lst.append(result)
#
#     elif '6' in num_lst[j]:
#         result = num_lst[j].replace('6', '-')
#         result_lst.append(result)
#
#     elif '9' in num_lst[j]:
#         result = num_lst[j].replace('9', '-')
#         result_lst.append(result)
#     else:
#         result_lst.append(num_lst[j])
#
# print(*result_lst)
