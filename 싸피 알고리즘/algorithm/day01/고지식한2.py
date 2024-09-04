def f(t, p):  # 패턴 p와 일치하는 구간의 시작 인덱스 리턴, 일치하는 경우가 없으면 -1 리턴
    N = len(t)
    M = len(p)
    for i in range(N - M + 1):  # 비교구간의 시작 위치
        for j in range(M):
            if t[i + j] != p[j]:
                break  # for j, 다음 글자부터 비교 시작
        else:  # for j가 중단없이 반복 되면
            return i  # 패턴을 찾은 경우 인덱스 반환
    return -1 # 못찾았다면 -1반환


t = 'TTTTTABCTTAATA'
p = 'TTA'
print(f(t, p))
t = 'ABCDEABCDEAAT'
p = 'TTA'
print(f(t,p))