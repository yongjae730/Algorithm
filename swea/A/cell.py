# import sys
# sys.stdin = open('input.txt','r')

# 세포 배열(cell)을 트레이(tray)의 중앙에 배치하는 함수
def cell_to_tray(cell, tray):
    # 세로 N, 가로 M 크기의 세포 배열을 트레이에 배치
    for i in range(N):
        for j in range(M):
            # 트레이의 중앙에 세포를 위치시킴
            tray[(col // 2) + i - 1][(row // 2) + j - 1] = cell[i][j]


# 트레이에서 세포의 정보를 수집하는 함수
def cell_information(tray, cell_info):
    # 트레이의 모든 좌표를 탐색
    for x in range(col):
        for y in range(row):
            # 세포가 존재하는 좌표(값이 0이 아닌 경우)
            if tray[x][y] != 0:
                # 해당 좌표와 세포 정보(세포 활성 시간, 위치, 다음 상태로 전환되는 시간)를 저장
                # ex. 2라면 4에서 초기 3에서 비활성화 2에서 활성화  1에서 활성화 + 퍼짐 0에서 죽음
                # 해당값 -1 에서 퍼진다. 그래서 x2해주었음
                cell_info.append([tray[x][y], x, y, tray[x][y] * 2])
    return


# 세포 배양 함수
def cell_culture(tray, cell_info, Time):
    # 재귀 만들어 보려다 실패한 흔적
    # if Time == 0:
    #     return

    q = []
    # 세포 정보를 하나씩 꺼내서 처리 (x, y 좌표, 세포 활성 시간, 다음 상태 전환 카운트)
    for i in range(len(cell_info)):
        q.append(cell_info[i])
    while Time > 0:
        # 세포 정보를 세포의 크기 별로 내림차순 정렬
        # 제출 할 땐 while 문 밖에 뒀는데 여기 두는게 맞다고 생각함 근데 왜 됨?
        # 안에 두고 제출 하니까 시간이 약 2배가 늘긴함
        # 근데 왜 밖에 둬도 되는지 잘 모르겠음 내일 강사님에게 물어볼 것
        q = sorted(q, key=lambda x: -x[0])
        # 시간 -1
        Time -= 1
        # 임시로 셀의 정보를 저장할 리스트
        temp_cell = []
        while q:
            bacteria = q.pop(0)
            # 박테리아의 3번 인덱스 -> 다음 상태 전환 카운트
            bacteria[3] -= 1
            # 세포의 시간이 다 되었고 세포가 퍼져야 한다면
            # 위에 서술했듯 생명력의 -1만큼의 시간이 되면 퍼져야함
            if bacteria[3] == bacteria[0] - 1:
                # 상하좌우 4 방향으로 퍼지도록
                for k in range(4):
                    nx, ny = bacteria[1] + dx[k], bacteria[2] + dy[k]
                    # 이동한 위치가 빈 곳이라면
                    if tray[nx][ny] == 0:
                        # 박테리아의 0번째 정보 즉, 세포의 생명력을 주변에 퍼트림
                        tray[nx][ny] = bacteria[0]
                        # 그 정보와 좌표를 임시 저장 셀에 추가
                        temp_cell.append([bacteria[0], nx, ny, bacteria[0] * 2])
            # 세포의 시간이 모두 다 되었으면 세포를 비활성화
            # elif가 아니라 if인 이유 -> 1의 생명력을 가진 세포의 경우
            # 퍼짐과 동시에 죽어야함
            if bacteria[3] == 0:
                bacteria[3] = -1
                tray[bacteria[1]][bacteria[2]] = -1
            else:
                # 세포가 활성화 되는 시간도 아니고 죽는 시간도 아닌 경우
                temp_cell.append(bacteria)

        # 새로운 세포 정보를 큐에 추가
        # 이 과정을 거치는 이유, 임시 리스트가 아니라 바로 큐에 저장하면 시간이 안가서 종료를 못함
        for r in range(len(temp_cell)):
            q.append(temp_cell[r])


# 상하좌우 이동을 위한 델타 리스트
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

# 테스트 케이스 수 T를 입력받음
T = int(input())
for tc in range(1, T + 1):
    # 세로 크기 N, 가로 크기 M, 배양 시간 K 입력
    N, M, K = map(int, input().split())
    # 세포 배열(cell)을 입력받음
    cell = [list(map(int, input().split())) for _ in range(N)]
    # K배 확장한 트레이의 크기 계산 (세로 col, 가로 row)
    row = (M + K) * 2
    col = (N + K) * 2
    # 확장된 크기의 트레이를 0으로 초기화
    tray = [[0 for _ in range(row)] for _ in range(col)]
    # 세포 배열을 트레이에 배치
    cell_to_tray(cell, tray)
    # 세포 정보를 저장할 리스트 초기화
    cell_info = []
    # 트레이에서 세포 정보를 수집
    cell_information(tray, cell_info)

    # 세포 배양 시작
    cell_culture(tray, cell_info, K)
    # 최종적으로 트레이에 남아 있는 세포의 수를 계산
    cnt = 0
    for i in range(col):
        for j in range(row):
            if tray[i][j] not in [0, -1]:
                cnt += 1
    # # 디버깅용
    # for w in range(col):
    #     print(*tray[w])
    print(f'#{tc} {cnt}')
