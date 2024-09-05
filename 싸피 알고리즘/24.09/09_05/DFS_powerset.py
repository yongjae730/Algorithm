def find_subsets_with_target(A, target):
    N = len(A)

    # 내부 함수 (부분 집합을 만들게 되는 재귀함수 DFS)
    def make_subset(i, subset):
        # 기저조건 : 원소를 모두 N번째 까지 포함한 경우
        if N == i:
            # 부분 집합의 합이 target 이 되는지를 확인
            total = 0
            for i in range(len(subset)):
                total += subset[i]
            if total == target:  # 부분집합의 합이 target이 된다면
                subsets.append(subset[:])

            return
            # 유도 조건(부분 집합을 만들게 되는 조건)
        # i번째 원소를 집합에 포함 O/X
        subset.append(arr[i])
        make_subset(i + 1, subset)

        subset.pop()
        make_subset(i + 1, subset)

    # 합이 target 이 되는 부분집합을 담을 리스트
    subsets = []
    make_subset(0, [])
    return subsets


# 집합 arr 에 대해 원소의 합이 10이 되는 부분집합을 모두 출력하라!
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

answer = find_subsets_with_target(arr, 10)

for subset in answer:
    print(subset)
