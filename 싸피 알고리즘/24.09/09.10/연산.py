from collections import deque

def bfs(N, M):
    visited = set()
    q = deque()
    q.append(N)
    visited.add(N)  # N을 방문 표시

    # 연산 횟수 카운트 변수
    cnt = 0
    while q:

        for _ in range(len(q)):
            value = q.popleft()
            if value == M:
                return cnt  # 연산 횟수

            # 연산 4가지로 다음 숫자 만들기!
            for nxt_value in [value + 1, value - 1, value * 2, value - 10]:
                # 중간 연산 결과가 1에서 1,000,000미만의 값인지 확인!
                if nxt_value > 1000001 or nxt_value < 1:
                    continue
                # 방문 체크(해당 값이 이전에 이미 방문 했었습니까?)
                if nxt_value not in visited:
                    q.append(nxt_value)
                    visited.add(nxt_value)
        cnt += 1
    return -1


T = int(input())
for tc in range(1, T + 1):
    # N : 현재 수 , M : 목표 수
    N, M = map(int, input().split())

    # N -> ... -> M 까지의 최소 연산을 출력(완전 탐색,BFS)
    result = bfs(N, M)
    print(f'#{tc} {result}')

# from collections import deque


# # N -> ... -> M 까지의 최소 연산을 출력! (완전탐색, BFS)
# def bfs(N, M):
#     visited = [0] * 1_000_001  # 방문 체크
#
#     q = deque()  # 큐
#     q.append(N)
#     visited[N] = 1  # N 을 방문 표시
#     # 연산 횟수 카운트 변수
#     cnt = 0
#     while q:
#         for _ in range(len(q)):
#             value = q.popleft()
#             if value == M:
#                 return cnt  # 연산 횟수
#             # 연산 4가지로 다음 숫자 만들기!
#             for n_value in [value + 1, value - 1, value * 2, value - 10]:
#                 # 중간 연산 결과가 1에서 1,000,000 미만의 값인지 확인!
#                 # 방문 체크 (해당 값이 이전에 이미 방문 했었습니까??)
#                 if 1 <= n_value <= 1_000_000 and not visited[n_value]:
#                     q.append(n_value)
#                     visited[n_value] = 1
#         cnt += 1
#     return -1
#
#
# # 첫 줄에 테스트 케이스의 개수가 주어지고,
# T = int(input())
#
# for tc in range(1, T + 1):
#     # 다음 줄부터 테스트 케이스 별로 첫 줄에 N과 M이 주어진다.
#     # 1<=N, M<=1,000,000, N!=M
#     N, M = map(int, input().split())
#
#     # N -> ... -> M 까지의 최소 연산을 출력! (완전탐색, BFS)
#     answer = bfs(N, M)
#     print(f"#{tc} {answer}")