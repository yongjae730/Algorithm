T = int(input())

for tc in range(1, T + 1):
    A, B = list(map(str, input().split()))

    a= A.replace(B,'a')


    print(f'#{tc} {len(a)}')