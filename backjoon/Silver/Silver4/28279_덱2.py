'''
1 X: 정수 X를 덱의 앞에 넣는다. (1 ≤ X ≤ 100,000)
2 X: 정수 X를 덱의 뒤에 넣는다. (1 ≤ X ≤ 100,000)
3: 덱에 정수가 있다면 맨 앞의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
4: 덱에 정수가 있다면 맨 뒤의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
5: 덱에 들어있는 정수의 개수를 출력한다.
6: 덱이 비어있으면 1, 아니면 0을 출력한다.
7: 덱에 정수가 있다면 맨 앞의 정수를 출력한다. 없다면 -1을 대신 출력한다.
8: 덱에 정수가 있다면 맨 뒤의 정수를 출력한다. 없다면 -1을 대신 출력한다.
'''
from collections import deque
import sys

N = int(sys.stdin.readline())

dq = deque()

for i in range(N):
    order = sys.stdin.readline()

    if order[0] == '1':
        dq.appendleft(int(order[2:-1]))
    elif order[0] == '2':
        dq.append(int(order[2:-1]))
    elif order[0] == '3':
        if len(dq)>0:
            print(dq.popleft())
        else:
            print(-1)
    elif order[0] == '4':
        if len(dq)>0:
            print(dq.pop())
        else:
            print(-1)
    elif order[0] == '5':
        print(len(dq))
    elif order[0] == '6':
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == '7':
        if len(dq)>0:
            print(dq[0])
        else:
            print(-1)
    elif order[0] == '8':
        if len(dq) > 0:
            print(dq[-1])
        else:
            print(-1)