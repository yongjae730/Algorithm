# deque(덱) : double-end queue

from collections import deque

q = deque()
# 삽입 enqueue
q.append(1)
q.append(2)
q.append(3)

# 삭제 deqeue
x = q.popleft()
print(x)

x = q.popleft()
print(x)

x = q.popleft()
print(x)