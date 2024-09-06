def quicksort(left, right):
    # QuickSort 알고리즘의 재귀적 호출에 사용될 피벗 요소를 설정
    pivot = arr[left]  # 현재 배열의 왼쪽 끝 요소를 피벗으로 설정
    i = left + 1  # 피벗보다 큰 값을 찾기 위한 오른쪽 인덱스
    j = right  # 피벗보다 작은 값을 찾기 위한 왼쪽 인덱스

    # 피벗을 기준으로 배열을 분할하는 과정
    while i <= j:
        # 피벗보다 작거나 같은 값을 찾기 위해 i 인덱스를 이동
        while i <= j and arr[i] <= pivot:
            i += 1
        # 피벗보다 크거나 같은 값을 찾기 위해 j 인덱스를 이동
        while i <= j and arr[j] >= pivot:
            j -= 1
        # i와 j가 교차되지 않았다면, 두 값을 교환
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # 피벗을 올바른 위치로 이동
    arr[left], arr[j] = arr[j], arr[left]

    # 피벗의 인덱스를 반환
    return j


def merge(left, right):
    # 재귀적 QuickSort 호출
    if left < right:
        pivot = quicksort(left, right)  # 피벗의 위치를 찾고, 배열을 두 부분으로 나눔

        # 피벗을 기준으로 왼쪽 부분과 오른쪽 부분을 정렬
        merge(left, pivot - 1)
        merge(pivot + 1, right)


T = int(input())  # 테스트 케이스의 수를 입력받음
for tc in range(1, T + 1):
    N = int(input())  # 배열의 크기를 입력받음
    arr = list(map(int, input().split()))  # 배열의 요소를 입력받음

    merge(0, len(arr) - 1)  # 전체 배열을 QuickSort로 정렬

    # 정렬된 배열의 중간값을 출력
    print(f'#{tc} {arr[N // 2]}')
