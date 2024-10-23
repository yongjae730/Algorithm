import sys

input = sys.stdin.readline


def binary_search(lan, n):
    start = 1
    end = max(lan)
    result = 0
    while start <= end:
        mid = (start + end) // 2

        cnt = 0
        for i in lan:
            cnt += i // mid

        if cnt < n:
            end = mid - 1
        else:
            result = mid
            start = mid + 1

    return result


K,N = map(int, input().split())

lan = []
for _ in range(K):
    len = int(input())
    lan.append(len)

result = binary_search(lan, N)

print(result)
