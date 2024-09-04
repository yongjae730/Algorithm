T = int(input())


for tc in range(1,T+1):
    memory = list(map(int,input().strip()))
    cnt = 0
    for i in range(len(memory)):

        if memory[i] == 1:
            for j in range(i,len(memory)):
                if memory[j] == 1:
                    memory[j] = 0
                else:
                    memory[j] = 1
            cnt += 1

    print(f'#{tc} {cnt}')