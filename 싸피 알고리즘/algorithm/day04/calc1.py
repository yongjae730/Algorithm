# 중위식 -> 후위식

# 중위식 표현의 값
expression = '(2+3)*4/5'  # input()

# 후위식 계산에 필요한 스택 초기화 (연산자들을 항상 우선순위가 더 높은 것이 위에 쌓이게)
stack = []
result = ''  # 후위식 표기법의 결과가 여기에 쌓인다.

for ch in expression:
    # 1.숫자일 때, 결과에 바로 추가
    # 2.'('일 때, 스택에 쌓는다. (우선순위가 가장 높기 때문)
    # 3.'*', '/' 일 때, 만약 * 와 / 가 있다면? pop을 한 뒤 스택에 쌓는다.
    # 4.'+', '-' 일 때, 만약 스택에 해당 연산 우선순위보다 더 높은게 있다면 모두 pop!
    # 그리고 스택에 쌓는다.
    # 5. ')' 일 때, 여는 괄호를 만날 때 까지 모두 pop을 하겠다.
    if ch.isnumeric():
        result += ch

    elif ch == '(':
        stack.append(ch)
    elif ch in ['*', '/']:
        if len(stack) > 0 and stack[-1] in ['*', '/']:
            result += stack.pop()
        stack.append(ch)
    elif ch in ['+','-']:
        while len(stack) > 0 and stack[-1] in ['*', '/','+','-']:
            result += stack.pop()
        stack.append(ch)
    elif ch == ')':
        while len(stack) > 0 and stack[-1] != '(':
            result += stack.pop()
        stack.pop() # 여는괄호 날려주기!

# 모든 순회를 다 하였을 때 스택에 남아있는 값은 결과에 추가
while len(stack)>0:
    result += stack.pop()

print(result)