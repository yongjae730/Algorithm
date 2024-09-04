import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt', 'w')

T = int(input())
for tc in range(1, T + 1):
    N = float(input())
    lst = [0 for _ in range(14)]
    cnt = 0
    A = 0

    while A != N:

        if cnt < (-13):
            break

        A += 1 * (2 ** (cnt))
        if A > N:
            A = A - (1 * (2 ** (cnt)))
            cnt -= 1

        else:
            lst[-cnt] = 1
            cnt -= 1

    if cnt < (-13) or lst[(-cnt)] == 1:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc} ', *lst[1:(-cnt)], sep='')
