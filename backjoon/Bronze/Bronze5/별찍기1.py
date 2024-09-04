import sys 

input = lambda: sys.stdin.readline().rstrip()

n = int(input())

for i in range(n+1):
    
    print("*"*int(i))