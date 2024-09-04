# DATA = [0, 4, 1, 3, 1, 2, 4, 1]
# COUNT = [0] * 5                      # DATA가 0~4까지의 정수 이기 때문에
#
# N = len(DATA)                       # DATA의 크기
# TEMP = [0] * N                      # 정렬된 결과 저장
#
# # 1단계:  DATA 원소별 개수 세기
# for x in DATA:                      # DATA의 원소 x를 가져와서 COUNT[x]의 개수 기록
#     COUNT[x] += 1
#
# # 2단계 : 각 숫자까지의 누적 개수 구하기
# for i in range(1, 5):               # COUNT[0]~COUNT[4] 까지 누적
#     COUNT[i] = COUNT[i-1] + COUNT[i]
#
# # 3단계 : DATA의 맨 뒤부터 TEMP에 정렬
# for i in range(N-1, -1, -1):
#     COUNT[DATA[i]] -= 1             # 누적 갯수 1개 감소
#     TEMP[COUNT[DATA[i]]] = DATA[i]
#
#
# print(*TEMP)



# # 카운트 배열 : 해당 수 (인덱스)의 빈도를 저장한 배열
# # 0<= x <= 10
# counts =[0] *11
# # 카운트 배열에 카운트(빈도수)를 누적
# for i in arr:
#     counts[i] += 1
#
# print(counts)
# # 해당 요소 i를 빈도수(seq) 만큼 출력해주면 되지롱!
# for x in range(0, 11):
#     seq = counts[x]
#     #빈도수 만큼 반복 수행
#     for _ in range(seq):
#         print(x, end = ' ')
# # 하지만 이 방법은 입력시의 순서를 보장해 주지않는다.



def counting_sort(arr):
    N = len(arr)
    # 카운팅 배열(초기화)
    counts = [0] * 101
    # arr 배열을 순회하면서 카운트 진행
    for i in range(len(arr)):
        x = arr[i]
        counts[x] += 1
    # 카운트 배열을 누적합으로 바꿔주기
    # for i : 1 -> N-1

    for i in range(1,N+1):
        counts[i] += counts[i-1]
    # (정렬) 원본 배열을 역순으로 순회하면서 정렬 진행
    # 저장해야할 필요가 있다면 임시배열을 원본 배열 크기 만큼 만든다.
    temp = [0] * N

    for i in range(N-1 , -1 , -1):
        x = arr[i] #요소 하나 가져오기
        # 누적합 배열에 해당 인덱스를 1 감소
        counts[x] -= 1
        # 누적합 배열의 값을 가지고 해당 위치(인덱스)에 x요소를 저장
        # j = counts[x]
        # temp[j] = x
        temp[counts[x]] = x

    return  temp


arr = [4, 5, 9, 0, 7, 1, 3, 2, 6, 8, 3, 5, 7, 6, 1, 6, 8]
result = counting_sort(arr)
print(*result)
# N 어디 넣어야..?
