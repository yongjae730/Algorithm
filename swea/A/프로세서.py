def check_core(arr):
    """
    2D 배열에서 값이 1인 위치(코어의 위치)를 찾아서 core_location 리스트에 추가한다.
    """
    global core_location
    for x in range(N):  # 배열의 모든 행을 순회
        for y in range(N):  # 배열의 모든 열을 순회
            if arr[x][y] == 1:  # 해당 위치의 값이 1이라면 (코어가 있는 경우)
                core_location.append([x, y])  # core_location 리스트에 위치 추가


def check_priority(core_location):
    """
    각 코어에 대해 연결 가능한 방향 수를 계산하여 우선순위를 부여한다.
    우선순위는 4에서 주변에 있는 코어의 수를 뺀 값으로 결정된다.
    """
    for j in range(len(core_location)):  # 모든 코어 위치를 순회
        cnt = 0
        for k in range(4):  # 상하좌우 4방향을 확인
            cx, cy = core_location[j][0] + dx[k], core_location[j][1] + dy[k]
            while 0 <= cx < N and 0 <= cy < N:  # 배열 범위 내에서
                if arr[cx][cy] == 1:  # 해당 방향에 다른 코어가 있다면
                    cnt += 1  # 연결할 수 없는 방향 수를 센다
                    break  # 더 이상 진행할 필요 없으므로 중단
                cx, cy = cx + dx[k], cy + dy[k]  # 다음 위치로 이동

        core_location[j].append(4 - cnt)  # 연결 가능한 방향 수를 우선순위로 추가


def check_length(location):
    """
    각 코어에 대해 전선을 연결할 때 필요한 길이를 계산하는 함수.
    가장 짧은 전선의 경로를 찾아 전선을 설치한다.
    """
    global core_location
    for i in range(len(location)):  # 각 우선순위 코어 리스트를 순회
        visited = [[0 for _ in range(N)] for _ in range(N)]  # 방문 여부를 기록할 배열 생성
        x, y, priority = location.pop()  # 코어의 위치와 우선순위를 가져옴
        short_stack = []  # 가장 짧은 전선 경로를 저장할 리스트
        mx_cnt = 999  # 전선의 최대 길이를 초기화

        for k in range(4):  # 상하좌우 4방향을 확인
            cnt = 0  # 현재 방향의 전선 길이
            stack = []  # 현재 방향의 경로를 저장할 스택
            cx, cy = x + dx[k], y + dy[k]  # 시작 위치 설정

            while 0 <= cx < N and 0 <= cy < N:  # 배열 범위 내에서
                if arr[cx][cy] == 0 and visited[cx][cy] == 0:  # 전선을 설치할 수 있는 경우
                    cnt += 1  # 전선 길이 증가
                    visited[cx][cy] = 1  # 해당 위치 방문 표시
                    stack.append([cx, cy])  # 경로를 스택에 추가
                elif arr[cx][cy] != 0:  # 다른 코어나 전선이 있으면 중단
                    stack = []
                    cnt = 999  # 불가능한 경우 큰 값으로 초기화
                    break

                cx, cy = cx + dx[k], cy + dy[k]  # 다음 위치로 이동

            if cnt < mx_cnt:  # 현재까지의 최소 전선 길이보다 짧다면
                mx_cnt = cnt
                short_stack = []  # 길이가 가장 짧은 경로로 업데이트
                for i in range(len(stack)):
                    short_stack.append(stack[i])

        # 가장 짧은 경로를 배열에 전선(값 2)로 표시
        for j in range(len(short_stack)):
            arr[short_stack[j][0]][short_stack[j][1]] = 2


# 메인 실행 코드 시작
T = int(input())  # 테스트 케이스의 수 입력

for tc in range(1, T + 1):
    N = int(input())  # 배열의 크기 입력
    arr = [list(map(int, input().split())) for _ in range(N)]  # N x N 크기의 배열 입력
    result = 0  # 결과를 저장할 변수

    # 상하좌우 이동을 위한 dx, dy 배열
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]

    # 각 코어의 위치를 저장할 리스트
    core_location = []

    # 우선순위에 따라 코어를 분류할 리스트
    core_priority_first = []
    core_priority_second = []
    core_priority_third = []
    core_priority_forth = []

    # 코어의 위치를 찾아 core_location에 저장
    check_core(arr)

    # 코어의 우선순위를 계산
    check_priority(core_location)

    # 가장자리 코어는 제외하기 위해 역순으로 체크 후 제거
    for i in range(len(core_location) - 1, -1, -1):
        if core_location[i][0] in [0, (N - 1)] or core_location[i][1] in [0, (N - 1)]:
            core_location.pop(i)

    # 코어를 우선순위에 따라 분류
    for k in range(len(core_location)):
        if core_location[k][2] == 1:
            core_priority_first.append(core_location[k])
        elif core_location[k][2] == 2:
            core_priority_second.append(core_location[k])
        elif core_location[k][2] == 3:
            core_priority_third.append(core_location[k])
        elif core_location[k][2] == 4:
            core_priority_forth.append(core_location[k])

    # 우선순위에 따라 전선을 연결
    check_length(core_priority_first)
    check_length(core_priority_second)
    check_length(core_priority_third)
    check_length(core_priority_forth)

    # 전선이 설치된 총 개수를 계산하여 결과로 출력
    result = 0
    for j in range(len(arr)):
        result += arr[j].count(2)  # 배열에서 값이 2인 (전선이 설치된) 위치의 개수를 센다

    print(f'#{tc} {result}')  # 테스트 케이스 번호와 결과 출력
