'''
명령은 총 여섯 가지이다.
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
from collections import deque
import sys
N = int(sys.stdin.readline())

q = deque()

for tc in range(0, N):
    order = sys.stdin.readline()

    if 'push' in order:
        q.append(int(order[5:-1]))
    elif 'front' in order:
        if len(q) > 0:
            print(q[0])
        else:
            print(-1)
    elif 'pop' in order:
        if len(q) > 0:
            print(q.popleft())
        else:
            print(-1)
    elif 'size' in order:
        print(len(q))
    elif 'empty' in order:
        if len(q) > 0:
            print(0)
        else:
            print(1)
    elif 'back' in order:
        if len(q) > 0:
            print(q[-1])
        else:
            print(-1)
