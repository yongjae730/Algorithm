import sys
sys.stdin = open("input.txt")

Tc = int(input())

for i in range(1, Tc+1):
    Tc_num = int(input())
    scores = map(int, input().split())
    fre_score = 0
    mx_score = 0

    for j in range(len(scores)):
        cnt_arr = [0] * 101
        for score in scores:
            if score in cnt_arr[j]:
                cnt_arr[j] += 1
