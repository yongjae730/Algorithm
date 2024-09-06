def dfs(n):
    global mx
    if n == cnt:
        temp = int(''.join(cards))
        if mx < temp:
            mx = temp
        return
    if (int(''.join(cards)),n) in used:
        return
    used.add((int(''.join(cards)),n))

    for i in range(len(cards)):
        for j in range(i + 1, len(cards)):
            cards[i], cards[j] = cards[j], cards[i]
            dfs(n + 1)
            cards[i], cards[j] = cards[j], cards[i]


T = int(input())
for tc in range(1, T + 1):
    cards, cnt = input().split()
    cnt = int(cnt)
    cards = list(cards)
    used = set()
    mx = 0
    dfs(0)
    print(f'#{tc} {mx}')