# import sys
#
# sys.stdin = open('algo1_sample_in.txt', 'r')
# sys.stdout = open('output.txt', 'w')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().strip()))

    # 가장 긴 길이부터 순회하기 위한 변수
    M = N
    # 결과 길이
    length = 0
    # 길이가 0 이 되거나 길이가 정해지면 while 종료
    # 가장 긴 길이부터 체크하기 때문에 더 작은 길이는 볼필요가 없기 때문
    while M > 0 and length == 0:

        for i in range(N - M + 1):
            # 한칸씩 앞으로 가면서 비교하기 위한 슬라이싱
            num = arr[i:i + M]
            # 만약 길이가 홀수 라면
            if len(num) % 2 != 0:
                # 비교를 진행
                if num == num[::-1]:
                    # 일치하면 길이 할당
                    length = len(num)
        # 가장 긴 길이부터 보기때문에 길이를 줄여준다.
        M -= 1

    print(f'#{tc} {length}')
