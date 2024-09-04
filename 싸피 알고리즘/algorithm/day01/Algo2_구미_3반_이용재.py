'''
언덕의 높이를 비교해서 앞의 언덕보다 높이가 높다면
arr에 넣고 그 경사도를 측정
그 경사도를 측정한 arr중 가장 긴 arr 출력
'''

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    hill = list(map(int, input().split()))
    arr = []
    arrs = []
    hill_degrees = []
    ssafy_hill = 9999999999

    # arr에 넣을 리스트를 만든다
    # arrs에 arr이 초기화 되기 전(높이가 낮아지기 전) 까지의 arr을 넣는다.
    for i in range(0, N + 1):

        if 0 <= i < N:
            if hill[i] > hill[i - 1] or hill[i] == hill[i - 1]:  # hill의 인덱스끼리 비교하여 같거나 더 크면 넣어준다.
                arr.append(hill[i])
        if i == N:  # 가장 끝의 수를 넣기위해서..
            arrs.append(arr)
        if i < N:
            if hill[i] < hill[i - 1]:
                arrs.append(arr)
                if not arr:
                    arrs.remove(arr)  # 빈 arr이 들어 오는 경우가 생겨 제거
                arr = []
            if not arr:
                arr.append(hill[i])

    for j in range(len(arrs)):
        if len(arrs[j]) > 1:
            hill_degree = (arrs[j][-1] - arrs[j][0]) / len(arrs[j])  # 경사도 측정
            if hill_degree <= ssafy_hill:
                ssafy_hill = hill_degree
                hill_degrees.append(ssafy_hill)
    mn_degree = 99999999999
    mn_index = 0
    mx_len = 0
    for k in range(len(hill_degrees)):
        if hill_degrees[k] <= mn_degree:
            mn_degree = hill_degrees[k]  # 경사가 가장 낮은 arr찾기
            mn_index = k  # 그 arr의 index를 넣는다.


    print(f'#{tc} {len(arrs[k])}')

