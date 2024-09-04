'''
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N ( 1 ≤ N ≤ 500 )이 주어진다.

다음 N개의 줄의 i번째 줄에는 두 정수 Ai, Bi ( 1 ≤ Ai ≤ Bi ≤ 5,000 )가 공백 하나로 구분되어 주어진다.

다음 줄에는 하나의 정수 P ( 1 ≤ P ≤ 500 )가 주어진다.

다음 P개의 줄의 j번째 줄에는 하나의 정수 Cj ( 1 ≤ Cj ≤ 5,000 ) 가 주어진다.
'''

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    bus_line = [0] * 5001
    for i in range(N):
        Ai, Bi = map(int, input().split())

        for k in range(Ai, Bi + 1):
            bus_line[k] += 1

    p = int(input())

    bus_stop = []

    for j in range(p):
        c = int(input())
        bus_stop.append(bus_line[c])

    print(f'#{tc}', *bus_stop)
