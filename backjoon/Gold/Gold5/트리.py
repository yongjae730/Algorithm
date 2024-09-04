# 노드를 삭제하고 자식 노드도 재귀적으로 처리하는 함수 정의
def tree(delete_node):
    # 삭제할 노드를 'deleted'로 마킹
    arr[delete_node] = 'deleted'

    # 삭제할 노드의 자식 노드를 재귀적으로 처리
    for i in range(N):
        if delete_node == arr[i]:
            tree(i)
N = int(input())
arr = list(map(int, input().split()))
delete_node = int(input())
# 삭제되지 않은 자식 없는 노드의 개수를 셀 변수 초기화
cnt = 0
# 주어진 삭제 노드와 그 자식 노드를 삭제 처리
tree(delete_node)
# 삭제되지 않고 자식이 없는 노드를 셈
for j in range(N):
    if arr[j] != 'deleted' and j not in arr:
        cnt += 1

# 자식 없는 남은 노드의 개수를 출력
print(f'{cnt}')

