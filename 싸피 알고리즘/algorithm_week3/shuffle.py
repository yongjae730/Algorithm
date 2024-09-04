T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cards = list(map(str, input().split()))
    shuffled_cards = []

    if N % 2 == 0:
        card1 = cards[:N // 2]
        card2 = cards[N // 2:]
        for i in range(len(card1)):
            shuffled_cards.append(card1[i])
            shuffled_cards.append(card2[i])
    else:
        card3 = cards[:N // 2 + 1]
        card4 = cards[N // 2 + 1:]
        for i in range(len(card4)):
            shuffled_cards.append(card3[i])
            shuffled_cards.append(card4[i])
        shuffled_cards.append(card3[-1])
    print(f'#{tc}', *shuffled_cards)
