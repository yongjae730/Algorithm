# 블록을 깨는 함수
def broke(cnt, total, board):
    global broken_block
    # 모든 블록을 깼을 경우 종료
    if total == block:
        broken_block = total
        return
    # 구슬을 다 쏜 경우 종료
    if cnt == 0:
        # 현재까지 깬 블록이 이전에 깬 블록보다 많을 경우 기록 갱신
        if total > broken_block:
            broken_block = total
        return

    # 각 열에 대해 구슬을 쏘는 시뮬레이션
    for i in range(W):
        # board 배열을 복사 (깊은 복사)
        arr = [x[:] for x in board]

        stack = []  # 구슬이 맞은 블록을 저장할 스택
        blocks = 0  # 깬 블록의 수
        # 해당 열에서 구슬이 처음 맞는 블록 찾기
        for row in range(H):
            if arr[row][i]:  # 블록이 있는 곳이면
                stack.append((row, i))  # 스택에 블록의 좌표 추가
                break

        # 스택이 빌 때까지 반복 (연쇄적으로 블록을 깸)
        while stack:
            row, col = stack.pop()  # 스택에서 블록 좌표를 꺼냄
            if not arr[row][col]:
                continue  # 이미 깬 블록이면 스킵
            blocks += 1  # 블록을 깼으므로 블록 수 증가
            # 블록이 깰 때 주변 블록도 연쇄적으로 깸 (arr[row][col] - 1 범위)
            for k in range(4):  # 4방향 (위, 아래, 왼쪽, 오른쪽)
                for l in range(1, arr[row][col]):  # 블록의 값만큼 파괴 범위 확장
                    nx, ny = row + dx[k] * l, col + dy[k] * l  # 새로운 좌표 계산
                    # 범위를 벗어나지 않고 블록이 있는 경우
                    if 0 <= nx < H and 0 <= ny < W and arr[nx][ny] != 0:
                        stack.append((nx, ny))  # 새로운 블록을 스택에 추가
            arr[row][col] = 0  # 블록을 깬 것으로 처리 (0으로 설정)

        # 블록을 깨고 난 후, 블록을 아래로 떨어뜨림 (중력 효과)
        for w in range(W):
            idx = H - 1  # 아래부터 채울 인덱스
            for h in range(H - 1, -1, -1):
                if not arr[h][w]:  # 빈칸이면 스킵
                    continue
                # 블록을 아래로 내리고 빈칸으로 만듦
                arr[idx][w], arr[h][w] = arr[h][w], arr[idx][w]
                idx -= 1
        # 구슬을 하나 덜 쏘고 재귀적으로 블록 깨기 진행
        broke(cnt - 1, total + blocks, arr)


# 입력 처리
T = int(input())  # 테스트 케이스 수

dx = [1, 0, 0, -1]  # 아래, 오른쪽, 왼쪽, 위 방향 배열
dy = [0, 1, -1, 0]  # 아래, 오른쪽, 왼쪽, 위 방향 배열

for tc in range(1, T + 1):
    # 구슬 쏘는 횟수 N, 가로 W, 세로 H
    N, W, H = map(int, input().split())
    # 게임판 블록 상태 입력
    board = [list(map(int, input().split())) for _ in range(H)]

    # 깬 블록 수 초기화
    broken_block = 0
    # 전체 블록 수 계산
    block = 0
    for x in range(H):
        for y in range(W):
            if board[x][y]:
                block += 1
    # N번 구슬을 쏘며 블록을 깨는 시뮬레이션 시작
    broke(N, 0, board)
    # 남은 블록 수 계산 (전체 블록 - 깬 블록)
    result = block - broken_block
    # 결과 출력
    print(f'#{tc} {result}')
