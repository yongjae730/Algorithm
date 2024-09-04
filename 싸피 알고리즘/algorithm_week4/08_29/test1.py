# 10진수 -> N진수 변환
def decimal_to_n(val):
    digit_to_alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []  # 나머지를 누적할 배열
    while val >= 2:
        val, remain = val // 2, val % 2
        result.append(digit_to_alpha[remain])  # 숫자 -> 문자
    result.append(digit_to_alpha[val])
    return '0'+''.join(result[::-1])


# N -> 10진수 변환
def n_to_decimal(val):
    return int(val, base = 16)


# N -> M 진수 변환
def n_to_m(val):
    num = n_to_decimal(val)  # N -> 10
    result = decimal_to_n(num)  # 10 -> M
    return result


T = int(input())
for tc in range(1,T+1):
    n,val = map(str, input().split())

    ans = n_to_m(val)

    print(ans)