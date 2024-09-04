def postfix(formula):
    result = ''
    post_stack = []

    for i in formula:
        if i.isnumeric():
            result += i

        elif i == '+':
            while len(post_stack) > 0 and post_stack[-1] in ['+','*']:
                result += post_stack.pop()
            post_stack.append(i)
        elif i == '*':
            if len(post_stack) > 0 and post_stack[-1] == '*':
                result += post_stack.pop()
            post_stack.append(i)
    while len(post_stack) > 0:
        result += post_stack.pop()
    return result


def calculate(postfix_formula):

    cal_stack = []
    for i in postfix_formula:
        if i.isnumeric():
            cal_stack.append(int(i))
        if i in ['*','+']:
            if i == '+':
                cal_stack[-2] = cal_stack[-2] + cal_stack[-1]
            elif i == '*':
                cal_stack[-2] = cal_stack[-2] * cal_stack[-1]
            cal_stack.pop()


    result = cal_stack[0]
    return result

T = 10

for tc in range(1, T + 1):
    N = int(input())
    formula = input()
    postfix_formula = (postfix(formula))


    print(f'#{tc} {calculate(postfix_formula)}')
