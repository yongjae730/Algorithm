# 정렬이 되어 있지 않은 배열(리스트)에서 원하는 값의 인덱스 찾기
def sequentialSearch(arr, N, target):
    '''
    정렬이 되어 있지 않은 배열에서 타겟(target)의 인덱스를 반환(없으면 -1)
    :param arr: 정렬되어 있지 않은 배열
    :param N: 배열의 길이
    :param target: 내가 찾고자 하는 값
    :return: target의 인덱스 (없으면 -1)
    '''
    for i in range(N):
        # 내가 찾고자 하는 target 값을 발견하면 해당 인덱스 반환
        if arr[i] == target:
            return i
    # 타겟 값을 찾지 못한 경우
    else:
        return -1  # for - else : 반복문을 완전히 실행 했을 때 else가 실행된다.
        # 내부에서 순회를 끝내면 발생하기 때문에 내부에 if등으로 return해 버리면
        # else를 실행하지 않게 한다


arr = [6, 4, 23, 12, 4, 6, 1, 2, 5, 0, 5]
result = sequentialSearch(arr, len(arr), 5)
print(result)
result = sequentialSearch(arr, len(arr), 10)
print(result)
