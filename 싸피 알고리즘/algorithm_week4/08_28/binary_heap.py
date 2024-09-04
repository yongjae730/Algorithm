from heapq import heappop, heappush, heapify
def inorder(node):
    global sum_num

    if node == 0:
        return sum_num

    sum_num += hq[node-1]
    inorder((node//2))



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    sum_num = 0
    hq = []
    for i in range(len(arr)):
        heappush(hq,arr[i])

    inorder(N)

    print(f'#{tc} {sum_num-hq[N-1]}')