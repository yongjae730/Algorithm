def check(node, N):
    global num
    if node > N:
        return 0
    if num[node] != 0:
        return num[node]
    num[node] = check(node * 2, N) + check(node * 2 + 1, N)
    return num[node]


T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    # N : 노드의 개수, M : 리프 노드의 개수 , L : 값을 출력할 노드
    num = [0] * (N + 1)

    for i in range(M):
        leaf, number = map(int, input().split())
        num[leaf] = number

    check(1, N)
    print(f'#{tc} {num[K]}')