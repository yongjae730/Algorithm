import sys
#input = sys.stdin.readline
input = lambda: sys.stdin.readline().rstrip()

t = int(input())

for i in range(1,t+1):
    a,b = map(int,input().split())
    print(a+b)