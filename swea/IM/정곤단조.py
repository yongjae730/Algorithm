def check(num):  # 단조 체크 하는 함수
    n = str(num)
    for i in range(len(n) - 1):
        if n[i] > n[i + 1]:
            return False

    return True


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    max_num = -1

    for i in range(N):
        for j in range(i + 1, N):
            num = arr[i] * arr[j]

            if max_num > num:
                break

            if check(num) == True:
                max_num = num

    print(f'#{tc} {max_num}')
