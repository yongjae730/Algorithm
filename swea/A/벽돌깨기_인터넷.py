'''
문제 해결 방법
1. 전체 map을 받아온 array에 좌표값이 존재한다면(block이 있다.) 충돌시켜주고
2. 최초 충돌한 block의 폭발세기 만큼 4방향벡터를 돌려주고 좌표값이 존재한다면
   폭발에 휘말린 block이므로 그들의 좌표를 stack에 넣어준다.
3. 폭발세기가 1인 block은 한 칸을 지우므로 고려하지 않아도 되나,
   폭발세기가 1 이상인 block이 존재한다면 최초 충돌한 block과 마찬가지로 폭발세기만큼
   4방향벡터를 돌려주고 좌표값이 존재한다면 stack에 추가시켜 준다.
4. 이를 반복하여 stack에 들어있는 폭발에 휘말린 block들이 모두 사라질때까지 while문을 돌려준다.
5. 다음 구슬을 발사하기 전 col의 위 아래를 계산해서 0이면 위 아래 index를 바꿔준다. (중력부분)
'''


def comb(cnt, total, block_maps):
    # 전역변수로 선언된 전체 벽돌 개수와 깨진 벽돌 개수를 참조하기 위해 global로 선언
    global total_blocks, broken_blocks

    # 만약 현재까지 깬 벽돌 수가 전체 벽돌 수와 같다면(즉, 모든 벽돌을 깼다면) 결과를 반환
    if total == total_blocks:
        broken_blocks = total  # 모든 벽돌이 깨졌으므로 깨진 벽돌 수를 갱신
        return

    # 구슬을 다 쏘았을 경우(구슬을 쏘는 횟수가 0이면) 결과를 반환
    if cnt == 0:
        # 현재까지 깬 벽돌 수가 기록된 최대 깨진 벽돌 수보다 많으면 갱신
        if total > broken_blocks:
            broken_blocks = total
        return

    # 구슬은 위에서 아래로 떨어지므로 깨질 수 있는 벽돌은 해당 열의 최상단에 있는 벽돌이다.
    # 따라서 가로 길이(W) 만큼 반복하면서 각각의 열에 구슬을 쏘는 상황을 시뮬레이션
    for i in range(W):
        # 게임판을 깊은 복사하여 이후에 수정이 되더라도 원본을 유지
        arr = [x[:] for x in block_maps]

        # 좌표가 엉키지 않도록 set을 사용하여 깰 벽돌의 좌표를 저장
        stack = set()

        # 구슬로 인해 깬 벽돌의 수를 저장할 변수
        blocks = 0

        # 해당 열에서 가장 위에 있는 벽돌을 찾기 위해 세로 방향으로 반복
        for row in range(H):
            if arr[row][i]:  # 만약 벽돌이 존재한다면
                stack.add((row, i))  # 그 벽돌의 좌표를 스택에 추가
                break  # 최상단 벽돌만 처리하면 되므로 반복문 탈출

        # 스택에 쌓인 벽돌을 하나씩 처리
        while stack:
            row, col = stack.pop()  # 스택에서 좌표를 꺼냄
            if not arr[row][col]:  # 만약 벽돌이 없으면 continue
                continue

            # 벽돌을 하나 깼으므로 blocks를 1 증가
            blocks += 1

            # 벽돌이 깨질 때, 그 벽돌의 숫자만큼 상하좌우로 영향을 줌
            for k in range(4):
                next_row, next_col = row, col
                # 벽돌의 숫자 - 1 만큼 해당 방향으로 퍼져나감
                for _ in range(arr[row][col] - 1):
                    next_row += dx[k]
                    next_col += dy[k]
                    # 좌표가 유효한 범위 내에 있으면 스택에 추가
                    if 0 <= next_row < H and 0 <= next_col < W:
                        stack.add((next_row, next_col))

            # 벽돌을 깬 후 그 좌표의 벽돌을 0으로 설정(빈 공간으로 처리)
            arr[row][col] = 0

        # 벽돌을 깬 후, 벽돌이 없는 공간을 채워야 함 (중력 효과)
        for y in range(W):
            idx = H - 1  # 제일 밑부터 벽돌을 채우기 위해 인덱스를 설정
            for x in range(H - 1, -1, -1):  # 아래에서 위로 벽돌을 이동
                if not arr[x][y]:  # 벽돌이 없으면 continue
                    continue
                # 벽돌이 있으면 아래쪽으로 이동
                arr[idx][y], arr[x][y] = arr[x][y], arr[idx][y]
                idx -= 1  # 다음 위치로 이동

        # 구슬을 하나 쐈으니 cnt를 감소시키고, 추가로 깬 벽돌 수를 더한 후 다시 재귀 호출
        comb(cnt - 1, total + blocks, arr)


# 테스트 케이스의 수를 입력 받음
T = int(input())

# 벽돌이 퍼지는 방향을 설정 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]  # 세로 방향 이동 (위, 아래)
dy = [0, 0, -1, 1]  # 가로 방향 이동 (왼쪽, 오른쪽)

# 테스트 케이스 수만큼 반복
for test_case in range(1, T + 1):
    # N : 구슬을 쏘는 횟수, W : 게임판 가로 길이, H : 게임판 세로 길이
    N, W, H = map(int, input().split())

    # 게임판의 상태를 입력 받음 (H개의 줄에 W개의 숫자가 들어감)
    block_maps = [list(map(int, input().split())) for _ in range(H)]

    # 전체 벽돌의 개수를 저장할 변수
    total_blocks = 0

    # 게임판을 순회하며 전체 벽돌 개수를 계산
    for i in range(H):
        for j in range(W):
            if block_maps[i][j]:  # 벽돌이 있는 경우
                total_blocks += 1  # 벽돌 수를 1 증가

    # 부순 벽돌 수를 저장할 변수 (초기값은 0)
    broken_blocks = 0

    # 구슬을 쏘는 과정을 시작 (N번 쏘는 과정 시뮬레이션)
    comb(N, 0, block_maps)

    # 남아 있는 벽돌의 수는 전체 벽돌 - 부순 벽돌 수
    answer = total_blocks - broken_blocks

    # 테스트 케이스 번호와 남은 벽돌 수를 출력
    print(f'#{test_case} {answer}')

