# 시작점 : 0번 점원 / 탑의 높이는 0부터 시작
# 끝점 (기저조건) : N명의 점원을 탑에 쌓을 지 말지 고려를 완료

# 명시된 조건 : 모든 점원을 쌓았는데, B이하인 경우를 고려하지 X
# - 문제조건에 이게 없으면 B 이하인 ans도 따로 만들어주어야 한다.

def recur(cnt, sum_height):
    global ans
    # 기저조건 가지치기
    if sum_height >= B:
        ans = min(ans, sum_height)
        return
    # 기저조건. 모든 점원을 탑을 쌓는데 고려 했는가?
    if cnt == N:
        return
    # 쌓는다
    recur(cnt + 1, sum_height + heights[cnt])
    # 안쌓는다
    recur(cnt + 1, sum_height)


T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    ans = 1e9  # 점원들을 쌓은 탑 중 B에 가장 가까운 높이를 저장
    recur(0, 0)
    print(f'#{tc} {ans - B}')
