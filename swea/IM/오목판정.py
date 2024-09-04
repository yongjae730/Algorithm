def check_five(n, lst):
    # 방향> 우 하 / 오른쪽 위 대각선 / 왼쪽 아래 대각선
    direction = [(0, 1), (1, 0), (1, -1), (1, 1)]
    # dir_idx = 0

    status = False
    for x in range(n):
        for y in range(n):
            # 현재 위치를 저장하여 새로운 사이클 돌때마다 초기화한다
            cx, cy = x, y
            # o를 만나면 카운트(새로운 사이클마다 초기화된다)
            count = 0
            # 방향을 돌아보기 위한 변수
            dir_idx = 0
            if lst[cx][cy] == 'o':
                # 현 상태가 True가 아닐때까지
                while not status:
                    # 방향 무한반복하지 않도록 제한
                    # 오목 완성했다면
                    if count == 4:
                        status = True
                        break
                    # 방향별로 다음 위치를 정한다
                    nx, ny = cx + direction[dir_idx][0], cy + direction[dir_idx][1]
                    # 보드를 벗어나지 않으며 다음 칸의 요소가 'o'면
                    if 0 <= nx < n and 0 <= ny < n and lst[nx][ny] == 'o':
                        # 현재 위치를 이동하고 카운트를 올린다
                        cx, cy = nx, ny
                        count += 1
                        # 사용하던 방향 초기화
                        dir_idx = 0
                    # 만약 위의 방향에서 찾지 못했을 경우 방향을 바꿔본다

            dir_idx = (dir_idx + 1) % 4
            if dir_idx == 3:
                break

    if status:
        return 'YES'
    return 'NO'


t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    c_board = [list(input()) for _ in range(N)]