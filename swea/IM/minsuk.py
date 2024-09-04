T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    lst = [i for i in range(N + 1)]
    student = list(map(int, input().split()))
    student.sort()

    for j in range(len(student)-1,-1,-1):
        if student[j] in lst:
            lst.pop(student[j])

    print(f'#{tc}', end=' ')
    for i in range(1, len(lst)):
        print(lst[i], end=' ')
    print()
