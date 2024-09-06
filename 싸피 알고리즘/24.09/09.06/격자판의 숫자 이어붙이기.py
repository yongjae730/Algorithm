def dfs(y, x, path):
    if len(path) == 7:
        result.add(path)  # 현재까지의 경로를 결과 set에 저장
        return
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < 4 and 0 <= nx < 4:
            dfs(ny, nx, path + arr[ny][nx]) # 문자열을 누적하면서 다음으로 이동


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    # 문자로 쓰면 합치기 더 쉽기 때문에 각 칸을 문자로 입력받음
    arr = [input().split() for _ in range(4)]
    # 중복 제거를 위해
    result = set()

    for i in range(4):
        for j in range(4):
            dfs(i, j, arr[i][j])

    print(f'#{tc} {len(result)}')