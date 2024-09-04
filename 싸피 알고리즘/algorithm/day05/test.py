# def backtrack(a, k, n):  # a : 주어진 배열, k 결정할 원소, n 원소 개수
#     c = [0] * MAXCANDIDATES
#
#     if k == n:
#         process_solution(a, k)  # 답이면 원하는 작업을 한다.
#
#     else:
#         ncandidates = construct_candidates(a, k, n, c)
#         for i in range(ncandidates):
#             a[k] = c[i]
#             backtrack(a, k + 1, n)
#
#
# def construct_candidates(a, k, n, c):
#     c[0] = True
#     c[1] = False
#     return 2
#
#
# def process_solution(a, k):
#     for i in range(k):
#         if a[i]:
#             print(num[i], end=' ')
#     print()
#
#
# MAXCANDIDATES = 2
# NMAX = 4
# a = [0] * NMAX
# num = [1, 2, 3, 4]
# backtrack(a, 0, 3)
# ---------------------------------------------------------------------------------
#
# for i1 in range(1, 4):
#     for i2 in range(1, 4):
#         if i2 != i1:
#             for i3 in range(1, 4):
#                 if i3 != i1 and i3 != i2:
#                     print(i1, i2, i3)

# ---------------------------------------------------------------------------------

# def backtrack(a, k, n):
#     c = [0] * MAXCANDIDATES
#
#     if k == n:
#         for i in range(0, k):
#             print(a[i], end=' ')
#         print()
#     else:
#         ncandidates = construct_candidates(a, k, n, c)
#         for i in range(ncandidates):
#             a[k] = c[i]
#             backtrack(a, k + 1, n)
#
#
# def construct_candidates(a, k, n, c):
#     in_perm = [False] * (NMAX + 1)
#
#     for i in range(k):
#         in_perm[a[i]] = True
#
#     ncandidates = 0
#     for i in range(1, NMAX + 1):
#         if in_perm[i] == False:
#             c[ncandidates] = i
#             ncandidates += 1
#     return ncandidates
#
#
# MAXCANDIDATES = 5
# NMAX = 5
# a = [0] * NMAX
# backtrack(a, 0, 3)
# ---------------------------------------------------------------------------------

# def f(i, K):  # bit[i]를 결정하는 함수
#     if i == K:  # 모든 원서에 대해 결정하면
#         s = 0
#         for j in range(N):
#             if bit[j]:  # bit[j]가 0이 아니면
#                 print(a[j], end=' ')
#                 s += a[j]
#         print(' : ', s)
#     else:
#         # bit[i] = 1
#         # f(i + 1, K)
#         # bit[i] = 0
#         # f(i + 1, K)
#         for j in [0,1]:
#             bit[i] = j
#             f(i+1, K)
#
# N = 3
# a = [1, 2, 3]  # 주어진 원소의 집합
# bit = [0] * N
#
# f(0, N)
# ---------------------------------------------------------------------------------

# def f(i, k, s, t):  # i 원소, k 집합의 크기, s i-1까지 고려된 합, t 목표
#     global cnt
#     global fcnt  # 함수를 몇번 순회했는지
#     fcnt += 1
#     if s> t: # 고려한 원소의 합이 찾는 합보다 큰경우
#         return
#     elif s == t:
#         cnt += 1
#         return
#     elif i == k: # 모든 원소 고려
#         return
#     # if i == k:
#     #     if s == t:
#     #         cnt += 1
#     else:
#         bit[i] = 1
#         f(i + 1, k, s + A[i], t)  # A[i]포함
#         bit[i] = 0
#         f(i + 1, k, s, t)   # A[i] 미포함
#
#
# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# N = 10
#
# key = 1
# cnt = 0  # 합이 key와 같은 부분집합의 수 수
# bit = [0] * N
# fcnt = 0
# f(0, N, 0, key)
# print(cnt, fcnt)
# ---------------------------------------------------------------------------------
# # 부분집합을 만드는 코드
# # 집합 A로 부터 부분집합 만들기!
# A = [1,2,3]
# N = len(A)
# # 해당 인덱스의 요소를 사용할지 유무 결정
# bits = [0] *N
#
#
#
# # 재귀함수 subset
# def subset(A,N,idx,bits):
#
#
#     """
#
#     :param A: 부분집합을 뽑을 집합
#     :param N: 부분집합의 요소 갯수
#     :param idx :재귀호출한 깊이 idx
#     :param bits : 해당 인덱스의 요소 포함 유무 (0/1)
#     :return:
#     """
#     # 기저 조건( 종료조건) idx가 배열의 길이 N만큼 되면 종료!
#     if idx == N:
#         # 부분집합에 속하는 원소들을 출력!
#         # => bits에 해당 인덱스의 값이 1인 요소를 출력!
#         total = 0 # 누적 변수
#         for i in range(N):
#             if bits[i] == 1: # 부분집합에 포함되는 원소 인덱스!
#                 total += A[i]
#                 # print(A[i], '' , end = '')
#         # print()
#         if total == 3:
#             for i in range(N):
#                 if bits[i] == 1:  # 부분집합에 포함되는 원소 인덱스!
#                     total += A[i]
#                     print(A[i], '', end='')
#             print()
#
#         return
#     # 해당 인덱스(idx) 요소를 포함하겠다
#     bits[idx] = 1
#     subset(A,N,idx + 1, bits)
#
#     # 해당 인덱스(idx) 요소를 포함하지 않겠다.
#     bits[idx] = 0
#     subset(A,N,idx + 1, bits)
#
#
# subset(A,N,0, bits)
# ----------------------------------------------------------------------------------------
# # 연습문제 2 코드
# # 부분집합을 만드는 코드
# # 집합 A 로부터 부분집합 만들기!
# A = [1, 2, 3,4,5,6,7,8,9,10]
# N = len(A)
# # 해당 인덱스의 요소를 사용할지 유무 결정
# bits = [0] * N
#
#
# # 재귀함수 subset
# def subset(A, N, idx, bits, total):
#     # 기저조건 (종료조건) : idx 가 배열의 길이N 만큼 되면 종료!
#     if idx == N:
#         # 만약 요소의 합이 10이라면.. 출력하겠다 (조건)
#         if total == 10:
#             for i in range(N):
#                 if bits[i] == 1:  # 부분집합에 포함되는 원소 인덱스!
#                     print(A[i], '', end='')
#             print()
#         return
#     #가지치기 : 내가 찾고자 하는 값보다 크게 된다면 종료!
#     if total>10:
#         return
#
#     # 재귀호출
#     # 해당 인덱스(idx) 요소를 포함하겠다.
#     bits[idx] = 1
#     subset(A, N, idx + 1, bits, total+A[idx])
#     #    //                포함x
#     bits[idx] = 0
#     subset(A, N, idx + 1, bits, total)
#
#
# subset(A, N, 0, bits, 0)
# -----------------------------------------------
# # 순열
# arr = [1,2,3]
# N = len(arr)
#
#
# # 순열 만들기
# def permutation(arr,N,i):
#     # 기저조건(종료) : i ==N
#     if i == N:
#         print(arr)
#         return
#
#     # 재귀호출
#     # 인덱스 i <-> j 요소를 서로 교환 (i<j<=N)
#     for j in range(i,N):
#         arr[i], arr[j] = arr[j], arr[i]
#         permutation(arr,N,i+1)
#         arr[j],arr[i] = arr[i],arr[j]
#
# permutation(arr,N,0)
# ------------------------------------
# # 방문체크로 순열 만들기
# arr = [1, 2, 3]
# N = len(arr)
# visited = [False] * N
#
#
# # 순열 만들기 (해당 요소 k 인덱스를 뽑게 된다면 visited 배열에 체크!)
# def permutation(arr, N, visited, i, result):
#     # 기저조건 (카드를 모두 뽑은 경우 종료)
#     if i == N:
#         print(result)
#
#     # 모든 카드 중에서 하나의 카드를 뽑기!
#     for k in range(N):
#         # 방문 체크를 하였는지...
#         if visited[k] == False:
#             # k 인덱스 카드 뽑기
#             visited[k] = True
#             result.append(arr[k])
#             permutation(arr, N, visited, i + 1, result)
#             # k 인덱스 카드 되돌려 놓기(복구)
#             visited[k] = False
#             result.pop()
#
#
# permutation(arr, N,visited, 0, [])
# ---------------------------------------------------------------------------
# 토너먼트 카드게임
# 분할정복을 활용해서 토너먼트 게임

# 입력
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
# T = int(input())
#
#
# def play(cards, player1, player2):
#     # 1은 가위, 2는 바위, 3은 보를 나타낸다
#     card1 = cards[player1]
#     card2 = cards[player2]
#     if (card1 == 1 and card2 == 2) \
#             or (card1 == 2 and card2 == 3) \
#             or (card1 == 3 and card2 == 1):
#         return player2
#     elif card1 == card2:
#         return player1
#     else:
#         return player1
#
#
# def tournament(cards, N, L, R):
#     # 기저조건 (종료조건)
#     if L == R:
#         return L  # 해당 사람이 부전승(우승)
#
#     # 조합
#
#     # 분할 (재귀 호출)
#     # 왼쪽 그룹 범위
#     player1 = tournament(cards, N, L, (L + R) // 2)
#     # 오른쪽 그룹 범위
#     player2 = tournament(cards, N, (L + R) // 2 + 1, R)
#
#     # 경기를 진행
#     return play(cards, player1, player2)
#
#
# for tc in range(1, T + 1):
#     # 다음 줄부터 테스트 케이스의 별로 인원수 N과
#     # 인원수 N
#     N = int(input())
#     # 다음 줄에 N명이 고른 카드가 번호순으로 주어진다. 4≤N≤100
#     cards = list(map(int, input().split()))
#
#     winner = tournament(cards, N, 0, N-1)
#     # 카드의 숫자는 각각 1은 가위, 2는 바위, 3은 보를 나타낸다.
#     # 로직
# # 출력
#     print(f'# {tc} {winner+1}')
