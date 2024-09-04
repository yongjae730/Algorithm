T = int(input())

for tc in range(1, T + 1):
    N, M = input().split()
    m = int(M)
    num = list(map(str, input().split()))
    number = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    num_dict = {}
    for i in number:
        num_dict[i] = 0
        for j in range(m):
            if num[j] == i:
                num_dict[i] += 1
    print(f'#{tc}')
    for k in number:
        for l in range(num_dict[k]):
            print(k,end = ' ')