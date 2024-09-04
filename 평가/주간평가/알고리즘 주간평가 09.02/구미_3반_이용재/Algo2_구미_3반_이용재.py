# import sys
#
# sys.stdin = open('algo2_sample_in.txt', 'r')
# sys.stdout = open('output.txt', 'w')


# 아스키코드로 얻은 10진수를 2진수로 바꾸기 위한 함수
def bin(num):
    result = ''
    while num > 0:
        # num을 2 몫나누기로 줄이면서, 나머지 나누기로 취한 값을 result에 삽입
        num, val = num // 2, num % 2
        result += str(val)

    return result


# 암호를 만들기 위한 중위탐색 함수
def binary(node):
    global result
    # 들어가는 깊이가 전체 길이보다 길면 return
    if int(node) > len(bin_num_reverse):
        return
    # left의 경우 node *2 가 된다
    binary(node * 2)
    # 1번노드로 시작했지만 인덱스의 값은 0번부터 이므로 -1해준다.
    result += bin_num_reverse[int(node) - 1]
    # right의 경우 node *2 +1 이 된다
    binary(node * 2 + 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    alphabet = list(map(str, input().strip()))
    real_result = []
    for i in range(len(alphabet)):
        # 아스키코드 알아내기
        num = ord(alphabet[i])
        # 이진수 추출
        bin_num = bin(num)
        # 노드에 넣는 순서를 위해 뒤집는다.
        bin_num_reverse = bin_num[::-1]
        # 결과물을 담기위한 문자열
        result = ''
        # 최상위 노드에서 실행
        results = binary(1)
        # 나온 결과물을 리스트에 담음
        real_result.append(result)
    print(f'#{tc}', *real_result)
