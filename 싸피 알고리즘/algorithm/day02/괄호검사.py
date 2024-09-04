

def bracket_check(text):
    global is_failed
    for idx in range(len(text)):
        ch = text[idx]
        # 1. 여는 괄호를 만난다 "(" -> 스택에 삽입 (push)
        if ch in ['(', '[', '{']:
            # 해당 여는 괄호를 스택에 삽입
            stack.append(ch)
        # 2. 닫는 괄호를 만난다. ")" -> 스택에서 삭제 (pop)
        elif ch in [')', ']', '}']:
            if len(stack) == 0:
                return False
            temp = stack.pop(-1)
            # 2-2. 스택이 비어 있는 경우에는 검사 실패 !
            bracket_mapping = {
                '(': ')',
                '[': ']',
                '{': '}'
            }
            if bracket_mapping[temp] != ch:
                # is_failed = True
                return False
            # 2-1. 괄호의 쌍이 "(" <-> ")" 짝이 맞는지.

        # 3. 해당 과정을 모두 순회 하였음에도
        # 스택에 괄호가 남아있다면 검사 실패!
    if len(stack) > 0:
        return False

    return True

T = int(input())
for tc in range(1,T+1):
    text = input()
    stack = []
    is_failed = False

    result = bracket_check(text)

    if result:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
