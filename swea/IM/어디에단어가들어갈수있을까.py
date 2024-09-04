'''
입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
다음 줄부터 각 테스트 케이스가 주어진다.
테스트 케이스의 첫 번째 줄에는 단어 퍼즐의 가로, 세로 길이 N 과, 단어의 길이 K 가 주어진다.
테스트 케이스의 두 번째 줄부터 퍼즐의 모양이 2차원 정보로 주어진다.
퍼즐의 각 셀 중, 흰색 부분은 1, 검은색 부분은 0 으로 주어진다.
'''

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    total = 0
    # 가로 순회
    for i in range(N):
        stack = []
        for j in range(N):
            if j == N-1 and arr[i][j] == 1:
                stack.append(1)
                if len(stack) == K:
                    total += 1
                    stack = []
                else:
                    stack = []
            elif arr[i][j] == 1:
                stack.append(1)
            elif arr[i][j] == 0:
                if len(stack) == K:
                    total += 1
                    stack = []
                else:
                    stack = []

    # 배열을 zip하여 가로순회만 2번 하면 가로+세로임
    arr2 = list(map(list, zip(*arr)))

    for k in range(N):
        stack2 = []
        for l in range(N):
            if l == N-1 and arr2[k][l] == 1:
                stack2.append(1)
                if len(stack2) == K:
                    total += 1
                    stack2 = []
                else:
                    stack2 = []
            elif arr2[k][l] == 1:
                stack2.append(1)
            elif arr2[k][l] == 0:
                if len(stack2) == K:
                    total += 1
                    stack2 = []
                else:
                    stack2 = []

    print(f'#{tc} {total}')
