import sys

# 입력과 출력을 파일에서 읽고 쓰기 위해서 sys.stdin과 sys.stdout을 설정합니다.
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


def binary(target, arr):
    # 이진 탐색을 수행하여 target이 arr에 있는지 확인합니다.
    cnt_right = 0  # 오른쪽 탐색을 시작한 여부를 나타내는 플래그
    cnt_left = 0  # 왼쪽 탐색을 시작한 여부를 나타내는 플래그
    start = 0  # 탐색 시작 인덱스
    end = len(arr) - 1  # 탐색 끝 인덱스

    # 이진 탐색 루프
    while start <= end:
        mid = (start + end) // 2  # 중간 인덱스 계산
        if target == arr[mid]:
            return 1  # target이 arr[mid]와 같으면 1을 반환
        elif target < arr[mid]:
            # target이 중간 값보다 작으면, 오른쪽으로 이동
            if cnt_left != 0:
                break  # 이전에 왼쪽으로 이동한 경우, 중단
            end = mid - 1  # 탐색 범위를 왼쪽 절반으로 줄임
            cnt_left = 1  # 왼쪽 탐색 시작 플래그 설정
            cnt_right = 0  # 오른쪽 탐색 플래그 리셋
        elif target > arr[mid]:
            # target이 중간 값보다 크면, 왼쪽으로 이동
            if cnt_right != 0:
                break  # 이전에 오른쪽으로 이동한 경우, 중단
            start = mid + 1  # 탐색 범위를 오른쪽 절반으로 줄임
            cnt_left = 0  # 왼쪽 탐색 플래그 리셋
            cnt_right = 1  # 오른쪽 탐색 시작 플래그 설정

    return -1  # target이 arr에 없는 경우 -1을 반환


T = int(input())  # 테스트 케이스의 수를 입력받음
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 배열 A와 B의 크기를 입력받음
    A = list(map(int, input().split()))  # 배열 A를 입력받음
    B = list(map(int, input().split()))  # 배열 B를 입력받음

    result = 0  # 배열 B의 각 요소가 배열 A에 존재하는 개수를 저장할 변수
    A.sort()  # 배열 A를 오름차순으로 정렬

    # 배열 B의 각 요소가 배열 A에 있는지 확인
    for i in range(len(B)):
        total = binary(B[i], A)  # 배열 A에서 B[i]를 이진 탐색하여 존재 여부 확인
        if total != -1:
            result += 1  # B[i]가 배열 A에 있으면 카운트를 증가

    # 결과를 출력 파일에 저장
    print(f'#{tc} {result}')
