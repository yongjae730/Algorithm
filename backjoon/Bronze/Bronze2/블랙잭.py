import sys
N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

n = len(numbers)
max = 0
for i in range(n):
    for j in range(i+1, n):   # 처음엔 범위 설정을 전부 n으로 했음 근데 i가 증가 한다면 그 이전의 수의 경우의 수는 이미 지났기 때문에
        for k in range(j+1, n): # 확인할 필요가 없기 때문에 점차 범위가 줄어들게 하는게 맞음 그리고 같은카드 3장 방지도 가능
            cards = numbers[i]+numbers[j]+numbers[k]
            if  cards<= M:
                if cards > max:
                    max = cards
print(max)