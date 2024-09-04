# 선형큐 ( 정적인 배열에 구현)
# 큐 : 선입선출의 형태를 띄는 자료형

# N 크기 만큼의 데이터를 저장하기 위한 배열 (초기화)
N = 10
queue = [0] * N
front = rear = -1  # 머리(front)와 꼬리(rear)를 각각 -1 초기화

# 큐가 비어있나
def isEmpty():
    # if front == rear:
    #     return True
    # else:
    #     return False
    return  front == rear
# 큐가 차있나
def isFull():
    # 꼬리의 위치가 배열의 끝 인덱스를 가리키면 꽉찼음
    # if rear == N-1:
    #     return True
    # else:
    #     return False
    return rear == N-1
# 큐 맨앞의 요소가 무엇인가

# 삽입 (enQueue)
def enqueue(x):
    global rear
    # 큐가 가득 차있다면 바로 종료
    if isFull():
        return
    # 꼬리를 한칸 증가 시켜주면서
    # 해당 위치에 요소 x 삽입
    rear += 1
    queue[rear] = x


# 삭제 (deQueue)
def dequeue():
    global front
    # 큐가 비어있다면 종료
    if isEmpty():
        return
    # 머리를 한칸 증가 시켜주면서
    # 해당 위치의 요소를 반환
    front += 1
    return queue[front]


enqueue(1)
enqueue(2)
enqueue(3)

x = dequeue()
print(x)
x = dequeue()
print(x)
x = dequeue()
print(x)

