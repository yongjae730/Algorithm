import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt', 'w')


def find_password(arr):
    for i in range(N):
        for j in range(M - 1, -1, -1):
            if arr[i][j] == '1':
                temp = arr[i][j:j - 56:-1]
                return temp


def check(arr):
    password = {
        '0001101': '0',
        '0011001': '1',
        '0010011': '2',
        '0111101': '3',
        '0100011': '4',
        '0110001': '5',
        '0101111': '6',
        '0111011': '7',
        '0110111': '8',
        '0001011': '9'
    }
    tmp1 = find_password(arr)
    tmp = tmp1[::-1]
    result = ''
    for i in range(0, len(tmp), 7):
        temp_pass = ''
        temp_pass += str(tmp[i]) + str(tmp[i + 1]) + str(tmp[i + 2]) + str(tmp[i + 3]) + str(tmp[i + 4]) + str(
            tmp[i + 5]) + str(tmp[i + 6])

        result += password[temp_pass]

    return result


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(str, input().strip())) for _ in range(N)]

    results = check(arr)
    sum_result1 = int(results[0]) + int(results[2])+int(results[4])+int(results[6])
    sum_result2 = int(results[1])+int(results[3])+int(results[5])

    final = sum_result1*3 + sum_result2 + int(results[-1])

    if final % 10 == 0:
        print(f'#{tc} {sum_result1+sum_result2+int(results[-1])}')
    else:
        print(f'#{tc} 0')
