# 테스트 케이스의 수를 입력 받음
T = int(input())
# 테스트 케이스 수만큼 반복
for tc in range(1, T + 1):
    # 문자열의 길이를 입력 받음
    N = int(input())
    # 검사할 문자열을 입력 받음
    word = input()
    # M은 N과 동일하게 초기화 (확인할 부분 문자열의 길이)
    M = N
    # 회문 길이를 저장할 변수 length 초기화
    length = 0
    # M이 0보다 크고, 회문이 발견되지 않은 동안 반복
    while M > 0 and length == 0:
        # 현재 길이 M의 부분 문자열을 검사
        for i in range(N - M + 1):
            # i부터 M까지의 부분 문자열 추출
            words = word[i:M+i]
            # 부분 문자열의 길이가 홀수인지 확인
            if len(words) % 2 != 0:
                # 부분 문자열이 회문인지 확인
                if words == words[::-1]:
                    # 회문이면 그 길이를 저장
                    length = len(words)
                    # 회문을 찾으면 반복문 탈출
                    break
        # M을 1 감소시켜 더 짧은 부분 문자열을 검사
        M = M - 1

    # 테스트 케이스 번호와 함께 회문의 길이를 출력
    print(f'#{tc} {length}')


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    word = input()
    M = N
    result = ''
    mx_len = 0
    while M > 0:
        for i in range(0, N - M + 1):
            result = word[i:i + M]
            if len(result) % 2 != 0:
                if result == result[::-1]:
                    ans = len(result)

                    if ans > mx_len:
                        mx_len = ans

        M -= 1

    print(f'#{tc} {mx_len}')
