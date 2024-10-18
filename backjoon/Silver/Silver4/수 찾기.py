# 자연수 N 입력
N = int(input())
# N 개의 정수 A[1], A[2], …, A[N]을 입력받아 정렬
arr = sorted(list(map(int, input().split())))
# 확인할 수 M 입력
M = int(input())
# M개의 수를 입력받아 리스트로 저장
target_lst = list(map(int, input().split()))

# target_lst의 각 수에 대해 반복
for i in target_lst:
    start = 0  # 이진 탐색 시작 인덱스
    end = len(arr) - 1  # 이진 탐색 끝 인덱스
    target = i  # 현재 탐색할 목표 값
    flag = False  # 목표 값을 찾았는지 여부를 저장하는 플래그

    # 이진 탐색 수행
    while start <= end:
        mid = (start + end) // 2  # 중간 인덱스 계산
        if arr[mid] == target:  # 중간 값이 목표 값과 같으면
            print(1)  # 존재하는 경우 1 출력
            flag = True  # 플래그를 True로 설정
            break  # 반복문 종료
        elif arr[mid] > target:  # 중간 값이 목표 값보다 크면
            end = mid - 1  # 오른쪽 범위를 줄임
        elif arr[mid] < target:  # 중간 값이 목표 값보다 작으면
            start = mid + 1  # 왼쪽 범위를 줄임

    if flag == False:  # 목표 값을 찾지 못한 경우
        print(0)  # 존재하지 않는 경우 0 출력
