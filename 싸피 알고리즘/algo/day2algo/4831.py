import sys
sys.stdin = open('bus_sample.txt')

T = int(input())

for i in range(1,T+1):
    K,N,M = map(int,input().split())
    charge = list(map(int,input().split()))
    bus_location = 0
    cnt = 0
    while bus_location:
        for j in range(N):
            if (bus_location + K) == charge[j]:
                cnt + 1
                bus_location = j

            elif (bus_location + K) != charge:
                    bus_location = (bus_location+ K - 1)


