import sys

sys.stdin = open('sample_input.txt')

T = int(input())  # 테스트 케이스

for i in range(1, T+1):

    N = int(input())    # 5<= N <= 100
    ai = list(map(int, input()))

    cnt_lst = [0] * 10
    for j in ai:
        cnt_lst[j] += 1

    mx_num = 0
    mx_fre = 0
# a = max(cnt_lst)
# b = cnt_lst.index(a)
    for k in range(len(cnt_lst)):
        if cnt_lst[k] >= mx_fre:
            mx_fre = cnt_lst[k]
            mx_num = k

    print(f'#{i} {mx_num} {mx_fre}')
