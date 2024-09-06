T = int(input())

for tc in range(1, T + 1):
    # N 컨테이너 수 , M 트럭 수
    N, M = map(int, input().split())
    freight = list(map(int, input().split()))
    volume = list(map(int, input().split()))
    result = 0
    if N < M :
        for i in range(N-1,-1,-1):
            difference = 999
            truck = 0
            for j in range(M-1,-1,-1):
                if volume[j] - freight[i] >= 0 and volume[j] - freight[i] < difference:
                    difference = volume[j] - freight[i]
                    truck = j
            freight.pop(i)
            result += volume.pop(truck)

    if N > M:
        for j in range(M-1,-1,-1):
            difference = 999
            truck = 0
            for i in range(N-1,-1,-1):
                if volume[j] - freight[i] >= 0 and volume[j] - freight[i] < difference:
                    difference = volume[j] - freight[i]
                    truck = i
            freight.pop(j)
            result += volume.pop(truck)
