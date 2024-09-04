# 동적인 크기를 가지고 있는 스택
stack = []

# 메인 동작 : push(삽입), pop(삭제)
def push(x):
    # x 값을 스택(리스트)에 맨 뒤에 삽입
    stack.append(x)

def pop():
    # 맨 뒤에 있는 값을 삭제 (+반환)
    return  stack.pop()

# isFull,isEmpty : 구현 필요 x
# isEmpty : 스택에 요소가 비어있다면

def isEmpty():
    # if not stack:
    #     return True
    # else:
    #     return False
    return not stack

# peek 가장 마지막에 삽입 했던 요소의 값 반환
def peek():
    return stack[-1]