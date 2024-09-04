import sys

sys.stdin = open('input/1216.txt')


def palindrom_check(word):
    mx_len = 0
    for j in range(len(word) // 2):
        if word[j] != word[-1-j]:
            return False

        if len(word) >= mx_len:
            mx_len = len(word)

    return mx_len


for tc in range(1, 11):
    N = int(input())
    words = [list(map(str, input())) for _ in range(100)]
    words2 = [[0 for _ in range(100)]for _ in range(100)]

    for x in range(100):
        for y in range(100):
            words2[x][y] = words[y][x]

    mx_palindrom = 0
    for x in range(100):
        for y in range(100):
            for i in range(49):
                if palindrom_check(words[x][y : y+i]):
                    if palindrom_check(words[x][y : y+i]) > mx_palindrom:
                        mx_palindrom = palindrom_check(words[x][y : y+i])

    for x in range(100):
        for y in range(100):
            for i in range(49):
                if palindrom_check(words2[x][y : y+i]):
                    if palindrom_check(words2[x][y : y+i]) > mx_palindrom:
                        mx_palindrom = palindrom_check(words2[x][y : y+i])
    print(f'{N} {mx_palindrom}')