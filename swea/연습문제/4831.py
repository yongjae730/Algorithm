T = int(input())
for i in range(0, T):
    K, N, M = list(map(int, input().split()))
    M_place = list(map(int, input().split()))
    cnt = K  # 내가 이만큼 갈 수 있음
    charge = 0  # 충전소 들려서 충전할대 카운트
    pre = 0  # 얘랑 같아지면 브레이크
    while cnt < N:
        if cnt == pre:
            charge = 0
            break
        if cnt in M_place:
            pre = cnt
            cnt += K
            charge += 1
        else:
            cnt -= 1

    print(f'#{i + 1} {charge}')
