# 입력
# 첫 줄에 테스트 갯수 T 가 주어진다.
T = int(input())

is_goal = False


def dfs(S, G):
    global is_goal
    # 나의 시작점 위치에 방문체크!
    visited[S] = True
    if S == G:
        is_goal = True
        return

    for nxt in adj[S]:
        # 기저 조건 : 이미 방문한 노드라면 제외
        if visited[nxt]:
            continue
        # 재귀 호출 : 다음 인접된 노드 -> G 계속 탐색
        dfs(nxt, G)


for tc in range(1, T + 1):
    # 다음 줄 부터 테스트 케이스의 첫 줄에 V와 E가 주어진다.
    # 노드의 갯수 V, 간선의 갯수 E
    V, E = map(int, input().split())
    # 테스트 케이스의 둘째 줄 부터 E개의 줄에 걸쳐, 출발 도착 노드로 간선정보가 주어진다.
    # 인접리스트 완성하기.
    adj = [[] for _ in range(V + 1)]
    for _ in range(E):
        # 출발 도착 노드로 간선정보가 주어진다. v ->u
        v, u = map(int, input().split())
        adj[v].append(u)
    # 출발 노드 s 와 도착노드 g가 주어진다.
    S, G = map(int, input().split())

    # 로직 (DFS 탐색을 통해 S -> ....-> G 경로가 존재하는지 확인!
    # 방문 체크를 위한 배열 .... visited
    visited = [False] * (V + 1)
    is_goal = False
    dfs(S, G)
    # 해당 시작지점에서 모든 DFS 순회를 완료했을 때
    # 도착지점에 방문체크가 되어있다면? -> 갈 수 있는 경로가 있는것.
    if visited[G]:
        result = 1
    else:
        result = 0
    # result = 1 if visited[G] == True else 0 -> 삼항연산자
    print(f'#{tc} {result}')
