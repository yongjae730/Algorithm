# N = 10
#
# q = [0] * N
# front = -1
# rear = -1
#
# rear += 1  # enqueue(1)
# q[rear] = 1
# rear += 1  # enqueue(2)
# q[rear] = 2
# rear += 1  # enqueue(3)
# q[rear] = 3
#
# front += 1
# print(q[front])  # dequeue()
# front += 1
# print(q[front])  # dequeue()
# front += 1
# print(q[front])  # dequeue()
#
# q2 = []
# q2.append(10)
# q2.append(20)
# print(q2.pop(0))
# print(q2.pop(0))
##
#####
# 원형 큐 구현
# Q_SIZE = 4
# cQ = [0]*Q_SIZE
# front = rear = 0
#
# rear = (rear+1)%Q_SIZE #enq(1)
# cQ[rear] = 1
#
# rear = (rear+1)%Q_SIZE #enq(2)
# cQ[rear] = 2
#
# rear = (rear+1)%Q_SIZE #enq(3)
# cQ[rear] = 3
#
# front = (front+1)%Q_SIZE
# print(cQ[front])
#
# front = (front+1)%Q_SIZE
# print(cQ[front])
#
# front = (front+1)%Q_SIZE
# print(cQ[front])
#
# rear = (rear+1)%Q_SIZE #enq(10)
# cQ[rear] = 10
#
# rear = (rear+1)%Q_SIZE #enq(20)
# cQ[rear] = 20
#
# rear = (rear+1)%Q_SIZE #enq(30)
# cQ[rear] = 30
#
#
# front = (front+1)%Q_SIZE
# print(cQ[front])
#
# front = (front+1)%Q_SIZE
# print(cQ[front])
#
# front = (front+1)%Q_SIZE
# print(cQ[front])


from collections import deque

deque_q = deque()
for i in range(1000000):
    deque_q.append(i)
for _ in range(1000000):
    deque_q.popleft()
print('end')