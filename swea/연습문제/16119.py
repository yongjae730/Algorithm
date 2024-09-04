import sys
sys.stdin = open('../input/16119.txt')

T = int(input())

for i in range(1, T+1):
    N = int(input())
    S = str(input())

    num_lst = []

    for j in range(N):
        num1 = '1' * j
        if num1 in S:
            num_lst.append(num1)
        else:
            continue

    print(f'#{i} {len(num_lst[-1])}')
