# 깊이 우선 탐색 (DFS) N-퀸 문제
# N-퀸 문제를 해결한 경우의 해의 갯수를 반환하는 함수
def n_queen_solve(N):
    # 중첩 함수 (내부 함수)
    def check(row,col):
        # 현재 행 row에 퀸을 배치한 후에 그 전까지의 퀸과 영역이 겹치는지를 검사
        # 퀸 i와 퀸 j가 같은 같은 대각선에 있는지 검사
        for i in range(row):
            if abs(i - row) == abs(queens[i] - col):
                return False
        return True

    def dfs(row):
        nonlocal result
        # 기저 조건 : 퀸을 N개 모두 배치하였을 때 종료
        if row == N:
            result += 1  # 해의 경우의 수를 1 증가
            return

            # 해당 행(row)에 대해 퀸을 열(col)에 배치
             # 대각선 검사(정대각선,역대각선) 검사
        for col in range(N):
            if visited[col] == False and check(row,col):
                visited[col] = True
                queens[row] = col
                dfs(row + 1)
                visited[col] = False

    # 초기화 (상태)
    # 퀸을 배치 할 수 있는 해의 갯수를 카운트
    result = 0
    # 퀸이 배치 되어 있는 상태를 나타내는 배열
    queens = [-1] * N
    visited = [False] * N  # 같은 열에 배치가 되지 않도록 체크
    dfs(0)

    return result


N = 4  # 퀸의 갯수 N

answer = n_queen_solve(N)
print(answer)
