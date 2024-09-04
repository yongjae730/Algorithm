import sys
sys.stdin = open('../input/1208.txt')

for i in range(1, 11):
    Dump = int(input())
    height = list(map(int, input().split()))


    for j in range(1, Dump+1):
        height.sort()
        height[0] += 1
        height[-1] -= 1
    height.sort()
    result = height[-1]-height[0]
    print(f'#{i} {result}')