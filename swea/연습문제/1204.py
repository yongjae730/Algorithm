import sys
sys.stdin = open('../input/1204.txt')

T = int(input())

for i in range(T):
    Tc = int(input())
    grade = list(map(int, input().split()))
    cnt = [0] * 101

    for j in grade:
        cnt[j] += 1

    mx_cnt = 0
    mx_num = 0
    for k in range(len(cnt)):
        if cnt[k] >= mx_cnt:

            mx_cnt = cnt[k]
            mx_num = k

    print(f'#{i} {mx_num}')
