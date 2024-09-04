def check(N, i, visited):
    global result
    # 모든 순회 끝
    if i == N:
        sum_num = 0
        # 마지막 사람 뒤에는 사람이 없기 때문에 -1해준다.
        for x in range(len(visited)-1):
            # 배열[앞사람][뒷사람]을 했을 시 위험도가 나온다.
            sum_num += danger[visited[x]-1][visited[x+1]-1]

        # if sum_num == 0:
        #     return
        if result > sum_num:
            result = sum_num

            return result
        return

    for j in range(N):
        if visited[j] == 0:
            # visited에 어떤 순서로 줄을 서있나 체크
            visited[j] = i+1
            check(N, i + 1, visited)
            # 나와서 다시 0으로 만들어줘야 재순회 가능
            visited[j] = 0


T = int(input())

for tc in range(1, T + 1):
    # 외계인의 수
    N = int(input())
    # 위험도 표시
    danger = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    # 결과
    result = 999
    check(N, 0, visited)



    print(f'#{tc} {result}')
