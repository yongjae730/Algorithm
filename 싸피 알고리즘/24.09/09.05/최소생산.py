def price(i, visited, total, N):
    global mn_production_price
    if i == N:
        if mn_production_price > total:
            mn_production_price = total
            return
    elif total > mn_production_price:
        return
    for j in range(N):
        if visited[j] == 0:
            visited[j] = 1
            price(i + 1, visited, total + arr[i][j], N)
            visited[j] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    mn_production_price = 99999
    price(0, visited, 0, N)

    print(f'#{tc} {mn_production_price}')