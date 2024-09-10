# make_set : 각 요소를 parent 배열에 자기 자신으로 초기화 하는 과정
def init_set(N):
    # N개 만큼 요소를 가질 수 있는 배열을 할당해당 요소 들을 각자 자기자신으로 초기화
    parent = [i for i in range(N)]
    return parent


# find_set : 가장 최상위의 부모(그룹의 대표)를 찾아라
def find_set(x):
    # 기저 조건 : 자기 자신이 부모라면 종료
    if x == parent[x]:
        return x
    parent[x] = find_set(parent[x])
    # (최상위 부모) 그룹의 대표자 부모로 변경(경로 압축)
    return parent[x]


# union : x와 y가 속한 두 그룹을 하나로 합쳐라
def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x != root_y:
        if root_x > root_y:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y


N = 5  # 요소의 개수
parent = init_set(N)

union(0, 1)
union(2, 3)
union(0, 2)
union(0, 4)
print(parent)
