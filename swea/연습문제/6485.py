import sys
sys.stdin = open('../input/6485.txt')


T = int(input())
for Tc in range(1, T+1):
    N = int(input())
    bus_stop = [0] * 5001
    for j in range(1, N+1):
        ai, bi = map(int, input().split())
        for q in range(ai, bi+1):
            bus_stop[q] += 1

    P = int(input())

    real_bus_stop = []
    for k in range(1, P+1):
        C = int(input())
        real_bus_stop.append(bus_stop[C])

    print(f'#{Tc}', *real_bus_stop)
