def dfs(month, sum_cost):
    global ans
    # 기저 조건. 12월까지 모두 보았는가.
    if month > 12:
        ans = min(ans, sum_cost)
        return
    # 1일권으로 모두 구매 (다음 재귀 :다음 달을 확인)
    dfs(month + 1, sum_cost + (days[month] * cost[0]))
    # 1달권 구매(다음 재귀 :다음 달을 확인)
    dfs(month + 1, sum_cost + cost[1])
    # 3달권 구매(다음 재귀 :3달 후 확인)
    dfs(month + 3, sum_cost + cost[2])
    # 1년권 구매(다음 재귀 :12달 후를 확인)
    dfs(month + 12, sum_cost + cost[3])
    # 사실 재귀에서 빼고 1월에 구입한 비용이랑 비교해도 된다


T = int(input())

for tc in range(1, T + 1):
    cost = list(map(int, input().split()))
    days = [0]+list(map(int, input().split()))
    ans = 1e9
    dfs(1, 0)
    print(f'#{tc} {ans}')

#
# T = int(input())
#
# for tc in range(1, T + 1):
#     cost = list(map(int, input().split()))
#     days = [0]+list(map(int, input().split()))
#     dp = [0] * 13
#
#     for i in range(1,13):
#         # 현재 달의 최소 비용을 계산
#         # 1~2월 까지는 이전달 +1일권/ 이전달 +1달권
#         # 이전달 + 1일권 구입/ 이전달 + 1달권/ 3달전에 3달권 구입 중 최소
#         dp[i] = min(dp[i-1] + (days[i]*cost[0]), dp[i-1] + cost[1])
#         # 인덱스 오류를 피하기 위해 3월 이후 계산을 따로 작성
#         if i >= 3:
#             dp[i] = min(dp[i], dp[i - 3] + cost[2])
#
#
#     result = min(dp[12],cost[3])
#     print(result)
#
