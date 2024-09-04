'''
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(5 ≤ N ≤ 20)이 주어진다.
다음 N개의 줄의 각 줄에는 길이 N인 문자열이 주어진다.
각 문자는 ‘o’또는 ‘.’으로, ‘o’는 돌이 있는 칸을 의미하고, ‘.’는 돌이 없는 칸을 의미한다.
'''

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(str,input().strip())) for _ in range(N)]

    dx = [0, 1, 1, 1]
    dy = [1, -1, 0, 1]
    result = False
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 'o':  # o를 만나야 탐색 시작
                for k in range(4):
                    cnt = 1
                    cx, cy = x + dx[k], y + dy[k]
                    while 0 <= cx < N and 0 <= cy < N and arr[cx][cy] == 'o':
                        cnt += 1
                        cx,cy = cx + dx[k], cy+dy[k]

                    if cnt == 5:
                        result = True

    if result == True:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')