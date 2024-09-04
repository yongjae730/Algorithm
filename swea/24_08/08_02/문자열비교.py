T = int(input())

for tc in range(1,T+1):
    word = input()
    words = input()

    if word in words:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')