# page31. 연습문제2
import sys

sys.stdin = open("graph.txt", "r")


def bfs(node):  # 선입 선출 구조인 queue 처럼 확욜할 것이다.
    q = [node]
    # q에 저장되는 데이터 : 다음에 처리할 데이터 (후보군)
    while q:  # 갈 수 있는곳이 없을 때까지
        now = q.pop(0)  # 가장 앞에 있는 데이터를 뽑는다.

        print(now, end=' ')  # 현재 노드 출력

        # 현재 정점에서 인접한 정점들을 확인
        for next_node in graph[now]:
            if visited[next_node]:  # 이미 방문한 정점이면 통과
                continue

            visited[next_node] = 1  # 방문 처리
            q.append(next_node)  # 후보군에 추가(순서가 되면 처리해주세요)


# 그래프를 만드는 코드는 DFS와 BFS가 똑같다.
# 핵심 : 무슨 노드를 먼저 탐색할 것인가!
#       - 갈 수 있으면 끝까지 가자 : DFS
#       - 특정 정점을 기준으로 퍼져나가면서 확인하자 : BFS
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]  # 인접 리스트로 저장
visited = [0] * (N + 1)
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited[1] = 1
bfs(1)
