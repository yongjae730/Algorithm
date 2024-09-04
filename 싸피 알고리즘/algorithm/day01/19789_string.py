'''
입력받은 N을 set 해서 중복 없애고, 그것을 키로 가지는 딕셔너리에 각각 0 할당 하고
M에 해당 알파벳이 있으면 cnt +1 해주고
카운트 횟수가 가장 높은것을 출력한다.
'''

T = int(input())
for tc in range(1, T + 1):
    N = list(map(str, input()))
    M = list(map(str, input()))
    set_N = set(N)
    dict_N = {}
    for i in set_N:
        dict_N[i] = 0
        for j in M:
            if i == j:
                dict_N[i] += 1
    mx_str = max(dict_N.values())
    print(f'#{tc} {mx_str}')