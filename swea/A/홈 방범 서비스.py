'''
운영비용 = K*K+(K-1)*(K-1)
예) K = 1 -> 1*1 +0*0 = 1
    k = 2 -> 2*2 + 1*1  = 5
도시 크기 N 하나의 집당 지불비용 M

'''
import sys
sys.stdin = open('input.txt')

def security(x, y):
    global location
    value = 0
    home = 0
    k = 0
    while k < N*2:
        k += 1
        cnt = 0

        for cx in range(N):
            for cy in range(N):
                if abs(cx-x) + abs(cy-y) < k:
                    if city[cx][cy] == 1:
                        cnt += 1

        price = k * k + (k - 1) * (k - 1)
        values = cnt * M - price
        if values >= 0:
            home = cnt

    return home


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]

    total = 0
    for x in range(N):
        for y in range(N):
            result = security(x,y)
            if result > total:
                total = result
    print(f'#{tc} {total}')
