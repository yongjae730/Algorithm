import sys

sys.stdin = open("GNS_test_input.txt")

# 입력
# 입력 파일의 첫 번째 줄에는 테스트 케이스의 개수가 주어진다.
T = int(input())
for _ in range(1, T + 1):
    # 그 다음 줄에 #기호와 함께 테스트 케이스의 번호가 주어지고 공백 문자 후 테스트 케이스의 길이가 주어진다.
    tc, N = input().split()
    "#1", "7041"
    # 그 다음 줄부터 바로 테스트 케이스가 주어진다.
    # 단어와 단어 사이는 하나의 공백으로 구분하며, 문자열의 길이 N은 100≤N≤10000이다.
    words = input().split()  # ["SVN", "FOR", "ZRO", ]

    # 로직
    # 2.로직 : 정렬 기준을 매직 테이블을 가지고 정수값을 기준으로 정렬하겠다!
    # words.sort(key=lambda w: alpha_to_integer[w])  # 오름차순(사전순)
    # sorted()
    #
    # print(f'{tc}', *words)
    # 문자열 -> 숫자값 (매직 테이블 구축)
    alpha_to_integer = {
        "ZRO": 0,
        "ONE": 1,
        "TWO": 2,
        "THR": 3,
        "FOR": 4,
        "FIV": 5,
        "SIX": 6,
        "SVN": 7,
        "EGT": 8,
        "NIN": 9
    }
    # 리스트 안의 요소를 문자열 -> 숫자로 변환
    for idx in range(len(words)):
        words[idx] = alpha_to_integer[words[idx]]
    # 정렬 (오름차순)
    words.sort()
    # 숫자값 -> 문자열 (매직 테이블 숫자 -> 문자)
    integer_to_alpha = {value: key for key, value in alpha_to_integer.items()}
    for idx in range(len(words)):
        words[idx] = integer_to_alpha[words[idx]]
    # 출력
    # print(f"{tc} {' '.join(words)}")
    print(f'{tc}', *words)