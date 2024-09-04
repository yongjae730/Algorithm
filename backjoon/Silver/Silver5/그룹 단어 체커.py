import sys


n = int(input())

cnt = n

for i in range(n):
    
    word = input()
    word1 = list(word)
    for j in range(0, len(word1)-1):   #len(word1) 까지 하면 마지막 j 번째 인덱스 뒤에 인덱스까지 탐색해야 하기 때문에 j -1 번째까지만 탐색한다
        
        if word1[j] == word1[j+1]:
        
            pass
        
        elif word1[j] in word1[j+1:]:

            cnt -= 1

            break

print(cnt)
