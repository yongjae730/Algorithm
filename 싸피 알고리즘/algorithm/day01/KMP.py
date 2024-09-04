def kmp(t, p):
    N = len(t)
    M = len(p)

    lps = [0] * (M + 1)
    # preprocessing
    j = 0  # 일치한 개수== 비교할 패턴 위치
    lps[0] = -1
    for i in range(1, M):
        lps[i] = j  # p[i] 이전에 일치한 개수  기록을 하고-> 비교하고 -> 다음 i를 비교하고 하는 방식
        if p[i] == p[j]:
            j += 1
        else:
            j = 0

    lps[M] = j
    # search
    print(lps)  # lps 출력 (할필요 없으나 확인차원에서 넣음)

    i = 0
    j = 0
    while i < N and j <= M:
        if j == -1 or t[i] == p[j]:
            i += 1
            j += 1
        else:
            j = lps[j]
        if j == M:
            print(i - M, end=' ')
            j = lps[j]
    print()
    return


t = 'zzzabcdabcdabcefabcd'
p = 'abcdabcef'
kmp(t, p)



