import sys
sys.stdin = open('../input/2001.txt')
T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    zone = [list(map(int, input().split())) for _ in range(N)]
    total = 0

    for x in range(N-M+1):
        for y in range(N-M+1):
            bugs = 0
            for i in range(M):
                for j in range(M):
                    bugs += zone[x+i][y+j]
            if total == 0:
                total = bugs
            if bugs > total:
                total = bugs
    print(total)
