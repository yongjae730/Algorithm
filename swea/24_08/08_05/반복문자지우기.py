T = int(input())

for tc in range(1,T+1):
    word = list(map(str,input().strip()))

    flag = True
    while flag:
        for i in range(len(word)-1):
            if word[i] == word[i+1]:
                word.pop(i)
                word.pop(i)
                flag = True
                break
        else:
            flag = False


    print(f'#{tc} {len(word)}')