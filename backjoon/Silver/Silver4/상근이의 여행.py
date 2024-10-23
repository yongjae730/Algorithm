T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    for _ in range(M):
        a, b = map(int, input().split())

    print(N - 1)
# 트리 문제지만 문제 오류로인해 인풋값 대충 받고 N-1 하면 풀리는 문제
