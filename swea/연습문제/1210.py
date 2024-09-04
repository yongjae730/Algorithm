for _ in range(10):
    N = int(input())

    ladder_list = [list(map(int, input().split())) for _ in range(100)]
    ci, cj = 99, ladder_list[99].index(2)

    di = [0, 0, -1]
    dj = [-1, 1, 0]

    while ci != 0:
        for k in range(3):
            ni, nj = ci + di[k], cj + dj[k]
            if 0 > ni or ni >= 100 or 0 > nj or nj >= 100:
                continue
            elif ladder_list[ni][nj] == 1:
                ladder_list[ci][cj] = 2
                ci, cj = ni, nj
                break

    print(f'#{N} {cj}')