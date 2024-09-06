# 방향 전환 규칙 (k값에 따른 이동 방향 변환)
# 위로 갈 때 (k = 0) -> 1,4,5 : 반사. 2 : 오른쪽으로 꺾음. 3 : 왼쪽으로 꺾음
# 아래로 갈 때 (k = 1) -> 2,3,5 : 반사. 1 : 오른쪽으로 꺾음. 4 : 왼쪽으로 꺾음
# 왼쪽으로 갈 때 (k = 2) -> 3,4,5 : 반사. 1 : 위로 꺾음. 2 : 아래로 꺾음
# 오른쪽으로 갈 때 (k = 3) -> 1,2,5 : 반사. 4 : 위로 꺾음. 3 : 아래로 꺾음

# import sys
#
# sys.stdin = open('input.txt', 'r')


def game(x, y, k):
    point = 0
    stx, sty = x, y  # 시작 좌표 저장
    while True:
        x += dx[k]  # 현재 방향에 따른 x 좌표 이동
        y += dy[k]  # 현재 방향에 따른 y 좌표 이동
        if (x, y) == (stx, sty) or board[x][y] == -1:  # 시작점으로 돌아오거나 블랙홀(-1)에 도달하면 종료
            return point
        if 1 <= board[x][y] <= 5:  # 블록을 만난 경우
            k = change_direction[board[x][y]][k]  # 현재 블록과 방향에 따른 방향 전환
            point += 1  # 포인트 증가
        elif 6 <= board[x][y] <= 10:  # 웜홀을 만난 경우
            x, y = wormhole_info[(x, y)]  # 연결된 웜홀 좌표로 이동


change_direction = [[],  # 0 - 상 1 - 하 2 - 좌 3 - 우
                    [1, 3, 0, 2],  # 1번 만났을 때
                    [3, 0, 1, 2],  # 2번 만났을 때
                    [2, 0, 3, 1],  # 3번 만났을 때
                    [1, 2, 3, 0],  # 4번 만났을 때
                    [1, 0, 3, 2]]  # 5번 만났을 때

T = int(input().strip())
dx = [-1, 1, 0, 0]  # x 좌표 이동: 상, 하, 좌, 우
dy = [0, 0, -1, 1]  # y 좌표 이동: 상, 하, 좌, 우
for tc in range(1, T + 1):
    N = int(input().strip())  # 보드 크기 입력
    wormhole_check = [(0, 0)] * 11  # 웜홀 체크용 배열 (6번 ~ 10번 웜홀 저장)
    wormhole_info = dict()  # 웜홀 연결 정보를 저장할 딕셔너리
    board = [[5] * (N + 2)]  # 보드 상단 외곽에 5번 블록(벽)을 추가한 배열
    mx_point = float('-inf')  # 최대 포인트를 저장할 변수

    # 보드 입력과 웜홀 정보 저장
    for i in range(1, N + 1):
        board.append([5] + list(map(int, input().strip().split())) + [5])  # 보드 양 끝에 5번 블록(벽)을 추가
        for j in range(N):
            num = board[i][j]
            if 6 <= board[i][j] <= 10:  # 웜홀 번호인 경우
                if wormhole_check[num] == (0, 0):  # 웜홀이 처음 발견되면 저장
                    wormhole_check[num] = (i, j)
                else:
                    # 두 번째 웜홀 발견 시 서로 연결 정보 저장
                    # 튜플로 넣지않으면 해시할당이 안되기 때문에 튜플로 넣는것.
                    wormhole_info[wormhole_check[num]] = (i, j)
                    wormhole_info[(i, j)] = wormhole_check[num]
    board.append([5] * (N + 2))  # 보드 하단 외곽에 5번 블록 추가

    # 빈 공간(0)에서 모든 방향으로 게임 진행
    for x in range(1, N + 2):
        for y in range(1, N + 2):
            if board[x][y] == 0:  # 빈 공간에서 시작
                for k in range(4):  # 상, 하, 좌, 우 4방향에 대해 게임 진행
                    total = game(x, y, k)  # 게임 진행 후 획득한 포인트 계산
                    if total > mx_point:  # 최대 포인트 갱신
                        mx_point = total
    #
    print(f'#{tc} {mx_point}')

    # # 디버깅용 코드 (필요 시 주석 해제)
    # for k in range(N+2):
    #     print(*board[k])
    #
    # print(wormhole_check)
    # print(wormhole_info)