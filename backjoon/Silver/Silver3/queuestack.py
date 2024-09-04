from collections import deque
import sys


def check(N, A, C, queuestack, cnt):
    global result
    for k in range(len(C)):
        queuestack.append(C[k])
        num = queuestack.popleft()
        result.append(num)



N = int(sys.stdin.readline())
A = deque(map(int, input().split()))
B = deque(map(int, input().split()))
M = int(sys.stdin.readline())
C = deque(map(int, input().split()))

queuestack = deque()

cnt = []
for q in range(len(A)):
    if A[q] == 0:
        cnt.append(q)

for i in range(len(cnt)-1,-1,-1):
    queuestack.append(B[cnt[i]])

result = []

check(N, A, C, queuestack, cnt)

print(*result)