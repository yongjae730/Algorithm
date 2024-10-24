import sys

input = sys.stdin.readline


def wifi(houses, c):
    start = 1
    end = max(houses) - min(houses)
    result = 0

    while start <= end:
        installed_house = []
        installed_house.append(min(houses))
        cnt = 1
        mid = (start + end) // 2
        for i in range(1, N):
            if houses[i] >= installed_house[-1] + mid:
                installed_house.append(houses[i])
                cnt += 1
            else:
                continue
        if cnt >= c:
            start = mid + 1
            result = mid
        # elif cnt < c:
        else:
            end = mid - 1
            # start = mid+1
    return result


N, C = map(int, input().split())
houses = []
for _ in range(N):
    house = int(input())
    houses.append(house)

houses.sort()
print(wifi(houses, C))
