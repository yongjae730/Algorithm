# """
# 3
# 5 1
# 2 1 2 5 1 6 5 3 6 4
# 5 1
# 2 6 6 4 6 5 4 1 5 3
# 10 5
# 7 6 7 4 6 9 4 11 9 5 11 8 5 3 5 2 8 1 8 10
# """
# # 후위순회 LRV
# # 카운트 변수 cnt(전역)
# def post_order(node): # 현재 노드 node
#     global cnt
#     if node == 0:
#         return
#     # 왼쪽 자식 탐색
#     post_order(left[node])
#     # 오른쪽 자식 탐색
#     post_order(right[node])
#     # 나 자신 탐색 (카운트 +1)
#     cnt += 1
#
#
# # 입력
# # 테스트 케이스 수 T
# T = int(input())
# for tc in range(1, T + 1):
#     # 첫 줄에 간선의 개수 E와 N이 주어지고, 다음 줄에 E개의 부모 자식 노드 번호 쌍이 주어진다.
#     E, N = list(map(int, input().split()))
#     data = list(map(int, input().split()))
#     # 노드 번호는 1번부터 E+1번까지 존재한다. 1<=E<=1000, 1<=N<=E+1
#     left = [0] * (E + 2)
#     right = [0] * (E + 2)
#     cnt = 0
#     for idx in range(E):
#         parent = data[idx * 2]
#         child = data[idx * 2 + 1]
#
#         if left[parent] == 0:
#             left[parent] = child
#         else:
#             right[parent] = child
#     # 로직
#     # 노드 N을 루트로 하는 서브 트리 안에 있는
#     # 모든 노드의 갯수를 카운트
#     # 순회... (전위/중위/후위 순회)
#     # -> 해당 트리 안에 모든 노드를 탐색하는 방법(기법)
#     # 후위 순회 노드 탐색 (LRV)
#
#
#     post_order(N)
#     # 출력
#     print(cnt)

# 의 테스트 케이스가 주어진다. (총 테스트 케이스의 개수는 입력으로 주어지지 않는다)
def in_order(node):
    if node == 0:
        return

    in_order(left[node])
    print(word[node],end = '')
    in_order(right[node])



T = 10

for tc in range(1, T + 1):
    # 입력
    # 정점의 총 갯수 N
    N = int(input())

    left = [0] * (N + 1)
    right = [0] * (N + 1)
    # 나의 노드에 들어있는 문자열 정보 일차원 배열
    word = [''] * (N + 1)
    # 그 다음 N 줄에 걸쳐 각각의 정점 정보가 주어진다.
    for _ in range(N):
        data = input().split()
        if len(data) == 4:
            node, ch, l_child, r_child = data
            node = int(node)
            word[node] = ch
            left[node] = int(l_child)
            right[node] = int(r_child)
        elif len(data) == 3:
            node, ch, l_child = data
            node = int(node)
            word[node] = ch
            left[node] = int(l_child)
        elif len(data) == 2:
            node, ch = data
            word[int(node)] = ch
    # 중위 순회
    print(f'#{tc}', end = ' ')
    in_order(1)
    print()
