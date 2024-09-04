# 선택정렬
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num_lst = list(map(int, input().split()))
    for i in range(N - 1):
        max_num = i
        min_num = i
        if i % 2 == 0:
            for j in range(i + 1, N):
                if num_lst[max_num] < num_lst[j]:
                    max_num = j
        num_lst[i], num_lst[max_num] = num_lst[max_num], num_lst[i]
        if i % 2 != 0:
            for j in range(i + 1, N):
                if num_lst[min_num] > num_lst[j]:
                    min_num = j
            num_lst[i], num_lst[min_num] = num_lst[min_num], num_lst[i]
    print(f'#{tc}', *num_lst[:10])
