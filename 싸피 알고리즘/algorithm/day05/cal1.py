# 강사님 코드
# 연산자 딕셔너리
operators = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y,
}
# 입력
T = 10
for tc in range(1, T + 1):
    # 각 테스트 케이스의 첫 번째 줄에는 문자열 계산식의 길이
    N = int(input())
    # 그 다음 줄에 문자열 계산식이 주어진다.
    infix = input()  # "9+8+5+9+2+4+1+8+3+9+3+8+7+8+6+8+9+4+1+1"
    # 로직 (중위 -> 후위)
    stack = []  # 스택 초기화 (연산자)
    postfix = []  # 후위연산식 (임시)

    # 중위 표현식을 순회하면서 후위표현식 만들기
    for ch in infix:
        # 피연산자(숫자)
        if ch.isnumeric():
            postfix.append(ch)
        # 연산자
        elif ch == '+':
            # 스택에 나보다 더 높은 우선순위가 있는지 확인!
            if len(stack) > 0:
                temp = stack.pop()
                postfix.append(temp)
            stack.append(ch)

    # 스택 안에 연산자가 남아있는 경우...
    while len(stack) > 0:
        temp = stack.pop()
        postfix.append(temp)

    # 후위 연산 계산
    stack = []  # 스택 초기화
    # 후위표기식을 순회하면서 연산 수행
    for ch in postfix:
        # 피연산자(숫자)
        if ch.isnumeric():
            # 스택에 추가
            stack.append(ch)
        # 연산자(-+*/)
        elif ch in '-+*/':
            if len(stack) < 2:  # ERR
                result = "error "
                break
            # 연산식을 통해 연산하기
            b = stack.pop()
            a = stack.pop()

            # 연산식 가져오기 (ch)
            operator = operators[ch]

            temp = operator(a, b)
            stack.append(temp)

    # 스택에 단 하나 남아있는 요소를 꺼낸다 (= 결과)
    result = stack.pop()
    # 출력
    print(f"#{tc} {result}")
