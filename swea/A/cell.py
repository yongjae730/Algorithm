import sys

sys.stdin = open('input.txt', 'r')


# 세포 배열(cell)을 트레이(tray) 중앙에 배치하는 함수
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
                # 해당 좌표와 세포 정보(위치, 세포 활성 시간, 다음 상태로 전환되는 시간)를 저장
                cell_info.append([x, y, tray[x][y], tray[x][y] + 1])
    return


def cell_culture(tray, cell_info):
    # 세포 정보를 하나씩 꺼내서 처리 (x, y 좌표, 세포 활성 시간, 다음 상태 전환 카운트)
    q = []

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
    row = M * K
    col = N * K
    # 확장된 크기의 트레이를 0으로 초기화
    tray = [[0 for _ in range(row)] for _ in range(col)]
    # 세포 배열을 트레이에 배치
    cell_to_tray(cell, tray)
    # 세포 정보를 저장할 리스트 초기화
    cell_info = []
    # 트레이에서 세포 정보를 수집
    cell_information(tray, cell_info)
    # 수집한 세포 정보 출력
    for i in range(len(tray)):
        print(*tray[i])
