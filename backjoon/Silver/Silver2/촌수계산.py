'''
부모 자식 관계를 나타내고(트리형태)
탐색을 해야하는 두 노드를 받았을 때
탐색을 총 몇번 시행해야 하는것인지.
트리 말고 다른방식은 안되나?

'''



N = int(input())
person1, person2 = map(int, input().split())
M = int(input())
adjL = [[] for _ in range(N + 1)]
# parent = [0 for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    adjL[u].append(v)
    adjL[v].append(u)
    # parent[v] = u
print(adjL)