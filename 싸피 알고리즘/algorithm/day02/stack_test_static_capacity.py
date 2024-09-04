# 강사님 수업

# 정적인 형태로 스택 구현
# 스택의 지정된 사이즈 size

SIZE = 10

# stack 과 top 위치를 초기화 하는 과정
stack = [0] * SIZE
top = -1


# 보조 연산 : isEmpty(스택이 비어있는지)
# 해당 top의 위치가 -1 위치에 있으면 == 스택이 비어있다.

def isEmpty():
    if top == -1:
        return True
    else:
        return False


# 보조 연산 : isFull (스택이 완전히 찼는지)

def isFull():
    # if top == SIZE -1:
    #     return  True
    # else:
    #     return False
    return top == SIZE - 1


# 보조 연산 : peek (맨 마지막에 삽입된 요소의 값),
def peek():
    return stack[top]


# 중요 연산 : push(삽입), pop(삭제)
# push 삽입 : 맨 마지막 위치에 값을 추가하기 위한 삽인
def push(x):
    global top
    # 스택이 가득 차 있다면 삽입 중단! (top의 위치가 SIZE -1)
    if isFull():
        return
    # top의 위치를 +1 증가
    top += 1
    # 해당되는 top위치에 스택 요소를 할당(추가)
    stack[top] = x


# pop 삭제 : 맨 마지막에 넣었던 요소를 제거!
# (+삭제된 요소의 값을 반환)
def pop():
    global top
    # 스택이 비어있다면 pop 과정을 중단.
    if isEmpty():
        return
    # 반환하고자 하는 값을 임시 변수로 저장
    temp = stack[top]
    # top의 위치를 1 감소시킨다.
    top -= 1

    return temp


push(1)
push(2)
push(3)
push(4)
push(5)
push(6)
push(7)
push(8)
push(9)
push(10)

x = pop()
print(x)  # 10
x = pop()
print(x)  # 9
x = pop()
print(x)  # 8
x = pop()
print(x)  # 7
x = pop()
print(x)  # 6
x = pop()
print(x)  # 5
x = pop()
print(x)  # 4
x = pop()
print(x)  # 3
x = pop()
print(x)  # 2
x = pop()
print(x)  # 1
