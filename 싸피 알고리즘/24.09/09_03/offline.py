# # 순열 만들기 재귀함수(교환)
# # nPr -> n 개의 요소 중에서 r 개를 선택하는 방법
# def permutation(arr, n, r, i):
#     if i == r:  # 종료 조건 ( 기저조건)
#         # r 개만큼 요소를 선택하였다면 종료!
#         for k in range(r):
#             print(arr[k], end=' ')
#         print()
#     # j값 순회 ...
#     for j in range(i, n):
#         # i,j를 교환
#         arr[i], arr[j] = arr[j], arr[i]
#         permutation(arr, n, r, i + 1)
#         # 복구
#         arr[j], arr[i] = arr[i], arr[j]
#
#
# arr = [1, 2, 3, 4]
# permutation(arr, 4, 4, 0)  # 4P4 = 4! = 24가지!
#
#
# # 순열 만들기 재귀함수 (방문체크)
# # nPr -> n개의 요소 중에서 r개를 선택 방법
# def permutation(arr, n, r, visited, result, i):
#     # 기저조건(종료조건) : i == r 이 되었을 때 종료
#     if i == r:
#         # 요소 r개를 선택한 내용을 출력
#         print(*result)
#         return
#     # 유도조건
#     # j : 0 -> n-1 [0, n) 순회
#     for j in range(0, n):
#         # 방문을 하였는지 확인(체크)
#         if visited[j] == 0:
#             # 방문 (결정)
#             visited[j] = 1
#             # result.append(arr[j])
#             permutation(arr, n, r, visited, result + [arr[j]], i + 1)
#             # 방문 (복구)
#             visited[j] = 0
#             # result.pop()
#
#
# arr = [1, 2, 3]
# N = len(arr)
# # 상태공간트리 내에서 루트노드에 적혀져 있는 상태(데이터)
# # 밖에서 초기화를 진행하고 함수에 전달해줘야한다.
# # 해당 카드 i번째를 선택하게된 임시 순열 리스트
# result = []
# # 방문체크를 위한 배열
# visited = [0] * N
# permutation(arr, N, 3, visited, result, 0)  # 3P3 = 3! = 6가지!
#
#
# # 조합 만들기 재귀함수 (방문체크)
# # 조합 : 순서가 없이 요소를 선택하는 방법
# # nCr -> n개의 요소 중에서 r개를 순서가 없이 선택 방법
# def combination(arr, N, visited, result, r, i):
#     # 기저조건( 종료조건)
#     if len(result) == r:
#         print(*result)
#         return
#     # 유도 조건 (재귀호출)
#     for j in range(i, N):
#         if visited[j] == 0:
#             visited[j] = 1
#             result.append(arr[j])
#             combination(arr, N, visited, result, r, j + 1)
#             visited[j] = 0
#             result.pop()
#
#
# arr = [1, 2, 3, 4]
# N = len(arr)
# visited = [0] * N
# result = []
# combination(arr, N, visited, result, 3, 0)  # 4C3 = 4개

## 부분 집합
def subset(arr, N, i):
    if i == N:
        for k in range(N):
            if bits[k] == 1:
                print(arr[k], end=' ')
        print()
        return

    # for j in range(0, 2):
    #     bits[i] = j
    #     subset(arr, N, i + 1)
    bits[i] = 0  # 결정
    subset(arr, N, i + 1)

    bits[i] = 1  # 결정
    subset(arr, N, i + 1)

arr = [1, 2, 3, 4]
N = len(arr)
bits = [0] * N
subset(arr, N, 0)
