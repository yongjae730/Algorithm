import sys

input = sys.stdin.readline


def cut_tree(trees, m):
    start = 0
    end = max(trees)
    result = 0
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for tree in trees:
            if mid > tree:
                continue
            else:
                total += (tree - mid)
        if total >= m:
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    return result



N, M = map(int, input().split())

trees = list(map(int,input().split()))
ans = cut_tree(trees,M)
print(ans)
