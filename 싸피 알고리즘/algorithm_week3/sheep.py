T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    number = set()
    cnt = 1
    while len(number) < 10:
        s = N * cnt

        string = str(s)
        for i in string:
            number.add(i)
        cnt += 1

    print(f'#{tc} {s}')
