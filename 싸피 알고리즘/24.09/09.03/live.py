# arr = ['O', 'X']
# path = []
#
#
# # lev 번째 요소
# def run(lev):
#     # 원소 3개를 모두고려함
#     if lev == 3:
#         print(path)
#         return
#
#     for i in range(2):  # 후보군(데려 갈지말지)
#         path.append(arr[i])  # 경로 추가
#         run(lev + 1)  # 다음 lev를 고려해라
#         path.pop()  # 경로 삭제
#
#
# run(0)
#
#
#
# arr = ['O', 'X']
# path = []
# name = ['MIN', 'CO', 'TIM']
#
#
# def print_name():
#     print('{', end=' ')
#     for i in range(3):
#         if path[i] == 'O':
#             print(name[i], end = ' ')
#     print("}")
#
# # lev 번째 요소
# def run(lev):
#     # 원소 3개를 모두고려함
#     if lev == 3:
#         print_name()
#         return
#
#     for i in range(2):  # 후보군(데려 갈지말지)
#         path.append(arr[i])  # 경로 추가
#         run(lev + 1)  # 다음 lev를 고려해라
#         path.pop()  # 경로 삭제
#
#
# run(0)
#


path = []


def dice(i,q):
    if i == 3:
        print(*path)
        return

    for j in range(q, 7):
        path.append(j)
        dice(i + 1,j)
        path.pop()


dice(0,1)
