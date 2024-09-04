# 라이브러리 (참고사항 : 알고리즘에서는 거의 사용 불가능)
# 순열과 조합을 뽑아낼 수 있음
from itertools import permutations, combinations

arr = [1, 2, 3]
# 순열
# 1,2,3
# 1,3,2
# 2,1,3
# 2,3,1
# 3,1,2
# 3,2,1
print(list(permutations(arr)))  # 모두 뽑아내서 순열 만들기
print(list(permutations(arr, 2)))  # 2개만 뽑아내서 순열 만들기
print(list(combinations(arr, 2)))  # 2개씩 뽑아내서 조합만들기

for comb in combinations(arr, 2):
    print(comb)

# 부분집합 = 조합을 통해서 만들 수가 있다.
# 조합을 0개부터 N개 까지 집합에서 뽑아내어 조합을 생성한다 = 부분 집합
N = len(arr)
for k in range(0, N + 1):
    for comb in combinations(arr, k):
        print(comb)
