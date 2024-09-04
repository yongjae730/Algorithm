from collections import deque
import sys

N = int(sys.stdin.readline())
dq = deque()
lst = []
balloon = list(map(int, sys.stdin.readline().split()))
for i in enumerate(balloon):
    dq.append(i)

while len(lst)<N :

    idx,num = dq.popleft()
    lst.append(idx+1)




