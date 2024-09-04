# '''
# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
# '''
#
#
# def bfs(s, V):  # 시작점 s , 종점 V
#     # 준비
#     visited = [0] * (V + 1)  # visited 생성
#     q = []  # queue 생성
#     q.append(s)  # 시작점 인큐
#     visited[s] = 1  # 시작점 방문 표시
#     # 탐색
#     while q:  # 탐색할 정점이 남아있으면
#         t = q.pop(0)    # t < - 디큐
#         print(t)    # 처리
#         for w in adj_l[t]:# t 에 인접이고 인큐된적이 없으면
#             if visited[w] == 0:
#                 q.append(w)    # 인큐하고 인큐됨 표시
#                 visited[w] = 1
#
# V, E = map(int, input().split())  # V는 마지막 정점, E는 간선 수
# arr = list(map(int, input().split()))
# # ----------인접리스트
# adj_l = [[] for _ in range(V + 1)]
# for i in range(E):
#     v1, v2 = arr[i * 2], arr[i * 2 + 1]
#     adj_l[v1].append(v2)
#     adj_l[v2].append(v1)
# # 여기까지 인접 리스트 -----------
# bfs(1, V)  # 출발점, 정점수
'''
7 8
4 2 1 2 1 3 5 2 4 6 5 6 6 7 3 7
'''


def bfs(s, V):  # 시작정점 s, 마지막 정점 V
    visited = [0] * (V + 1)  # visited 생성
    q = []  # 큐 생성
    q.append(s)  # 시작점 인큐
    visited[s] = 1  # 시작점 방문표시
    while q:  # 큐에 정점이 남아있으면 front != rear
        t = q.pop(0)  # 디큐
        print(t)  # 방문한 정점에서 할일
        for w in adj_l[t]:  # 인접한 정점 중 인큐되지 않은 정점 w가 있으면
            if visited[w] == 0:
                q.append(w)  # w인큐, 인큐되었음을 표시
                visited[w] = visited[t] + 1


V, E = map(int, input().split())  # 1번부터 V번 정점, E개의 간선
arr = list(map(int, input().split()))
# 인접리스트 -------------------------
adj_l = [[] for _ in range(V + 1)]
for i in range(E):
    v1, v2 = arr[i * 2], arr[i * 2 + 1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)  # 방향이 없는 경우
# 여기까지 인접리스트 -----------------
bfs(1, V)
