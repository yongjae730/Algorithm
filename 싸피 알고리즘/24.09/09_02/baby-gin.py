T = int(input())

for tc in range(1, T + 1):
    cards = list(map(int, input().strip()))

    cards.sort()

    run_cnt = False
    triplet_cnt = False
    for i in range(len(cards)-2):
        if cards[i] == cards[i+1] == cards[i+2]:
            run_cnt = True
        else:
            continue

    for i in cards:
        if cards.count(i) == 3:
            triplet_cnt = True
        else:
            continue

    if run_cnt == True and triplet_cnt == True:
        print('true')
    else:
        print('false')