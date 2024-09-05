def check(N, i, visited):
    global result


    # 모든 순회 끝
    if i == N:
        sum_num = 0
        print(visited)
        for x in range(len(visited)):
            if x != len(visited)-1:
                sum_num += battery[visited[x]-1][visited[x+1]-1]
            else:
                sum_num += battery[visited[x] - 1][visited[0] - 1]
        if result > sum_num:
            result = sum_num


            return result
        return


    visited[0] = 1
    for j in range(N):
        if visited[j] == 0:
            visited[j] = i+1
            check(N, i + 1, visited)
            visited[j] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    battery = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 2000
    check(N, 1, visited)



    print(f'#{tc} {result}')
