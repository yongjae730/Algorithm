def count_word(arr):
    global cnt
    stack = []
    for x in range(N):
        for y in range(N):

            if arr[x][y] == 1:
                stack.append(1)
            elif arr[x][y] == 0:
                if len(stack) == M:
                    cnt += 1
                stack = []

        if len(stack) == M:
            cnt += 1
            stack = []
        else:
            stack = []


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr2 = list(map(list, zip(*arr)))
    cnt = 0

    count_word(arr)
    count_word(arr2)

    print('#{} {}'.format(tc, cnt))
