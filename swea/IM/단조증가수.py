'''
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(1 ≤N ≤ 1,000) 이 주어진다.
두 번째 줄에는 N개의 정수 A1, …, AN(1 ≤ Ai ≤ 30,000) 이 공백 하나로 구분되어 주어진다.
'''


def check_num(number):
    num = str(number)
    for i in range(0, len(num) - 1):
        if num[i] > num[i + 1]:
            return False

    return True


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    # 뒤에서 부터 계산하기 위해 뒤집어줌
    arr.sort(reverse=True)
    # 최대 단조 증가수 설정
    mx_num = -1
    for i in range(N):
        for j in range(i + 1, N):
            number = arr[i] * arr[j]

            # 찾은 단조 증가 수보다 작다면 볼 필요 없음
            if mx_num > number:
                break
            # 단조 증가 체크 함수를 통과한게 True라면 mx_num과 비교하여 바꾼다.
            if check_num(number) == True:
                mx_num = number

    print(f'#{tc} {mx_num}')
