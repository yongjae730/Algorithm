'''
2
2
1 3
2 5
5
1
2
3
4
5
2
1 3
2 5
5
1
5
4
3
2

'''
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    bus_stop = [0] * 5001
    for i in range(N):
        A, B = map(int, input().split())

        for j in range(A, B + 1):
            bus_stop[j] += 1

    P = int(input())
    print(f'#{tc}', end=' ')
    for k in range(P):
        C = int(input())

        print(f'{bus_stop[C]}', end=' ')
    print()