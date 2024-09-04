T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    C = [-1] + list(map(int, input().split()))

    # 로직 (피자 굽기 시뮬레이션)
    # 화덕(FIFO)큐 - 동적인 형태로 리스트를 통해서
    furnace = []
    ready = list(range(1, M + 1))  # 다음 구울 피자 목록 (큐)
    # 1. 모든 피자를 다 구울 때까지 반복하겠다.
    # (아직 구우지 않은 피자, 화덕내에 피자가 없게끔 반복)
    while len(furnace) > 0 or len(ready) > 0:

        if len(furnace) > 0:
            # (2) 피자를 하나 빼겠다!
            pizza_idx = furnace.pop(0)
            # 2.1 치즈의 양을 절반 줄이겠다.
            C[pizza_idx] = C[pizza_idx] // 2
            # 2.2 해당 치즈량을 확인해줘야 한다!
            if C[pizza_idx] != 0:
                # 다시 화덕에 피자를 넣는다.
                furnace.append(pizza_idx)
        # (1) 피자를 화덕에다가 하나 넣겠다! (용량 N까지만)

        while len(ready) > 0 and len(furnace) < N:
            pizza_idx = ready.pop(0)
            furnace.append(pizza_idx)

    # 출력
    print(f'#{tc} {pizza_idx}')