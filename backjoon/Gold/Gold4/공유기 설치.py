import sys

input = sys.stdin.readline


def wifi(houses, c):
    start = 1
    end = max(houses) - min(houses)
    installed_house = []
    result = 0

    installed_house.append(min(houses))
    installed_house.append(max(houses))

    while start <= end:
        distance = 0
        mid = (start + end) // 2
        for i in range(1, N - 1):

            if houses[i] - mid > 0:
                ...


N, C = map(int, input().split())
houses = []
for _ in range(N):
    house = int(input())
    houses.append(house)

houses.sort()
wifi(houses, C)
