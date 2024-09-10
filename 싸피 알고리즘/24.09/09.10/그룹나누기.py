def make_set(N):
    parent = [i for i in range(N)]
    return parent


def find_set(x):
    if x == parent[x]:
        return x

    parent[x] = find_set(parent[x])
    return parent[x]
    # return parent[x]

def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:
        parent[root_y] = root_x


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    parent = make_set(N)
    lst = list(map(int, input().split()))
    for i in range(0, len(lst), 2):
        x = lst[i] -1
        y = lst[i + 1] -1
        union(x, y)
    for j in range(len(parent)):
        find_set(j)
    result = len(set(parent))
    print(f'#{tc} {result}')
