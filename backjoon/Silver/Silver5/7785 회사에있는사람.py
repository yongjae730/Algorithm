# import sys

# n = int(sys.stdin.readline())
# worker = []

# for i in range(n):
#     name,work =map(str,sys.stdin.readline().split())
#     if 'enter' in work:
#         worker.append(name)
#     if 'leave' in work:
#         worker.pop(name)

# worker.sort()
# worker.reverse()

# for j in range(len(worker)):
    
#     print(worker[j])

# 시간초과

import sys

n = int(sys.stdin.readline())
record = {}

for i in range(n):
    name,work =map(str,sys.stdin.readline().split())
    if 'enter' in work :
        record[name] = work
    if 'leave' in work:
        record.pop(name,work)

worker = list(record.keys())

worker.sort()
worker.reverse()

for j in range(len(worker)):

    print(worker[j])