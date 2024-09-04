import sys

sys.stdin = open('sample_input.txt')

T = int(input())


def Binary(P, Page):
    start = 1
    end = P
    cnt = 1

    while start <= end:
        cnt += 1

        middle = (start + end) // 2
        if middle == Page:
            return cnt
        elif middle > Page:
            end = middle
        else:
            start = middle

    return cnt


for i in range(1, T + 1):
    '''
    P : 전체 쪽수
    Pa : A가 찾을 쪽 번호
    Pb : B가 찾을 쪽 번호
    '''
    P, Pa, Pb = map(int, input().split())

    A = Binary(P, Pa)
    B = Binary(P, Pb)

    if A > B:
        print(f'#{i} B')
    elif A < B:
        print(f'#{i} A')
    elif A == B:
        print(f'#{i} 0')
