# # 11 12 13 21 ...
#
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f'{i}{j}')
#
# # 1111.1112.1113,1114....3333
# for i in range(1, 4):
#     for j in range(1, 4):
#         for k in range(1, 4):
#             for l in range(1, 4):
#                 print(f'{i}{j}{k}{l}')


# def KFC(x):
#     KFC(x + 1)
#
# KFC(0)
# RecursionError : Maximuim recursion depth exceeded 에러 발생
# def KFC(x):
#     if x == 6:
#         return
#     print(x)
#     KFC(x + 1)
#     print(x)
#
# KFC(1)
def path(x, visited):
    global cnt
    dice = 0
    if x == 3:
        for i in range(len(result)):
            dice += result[i]

        if dice <= 10:
            print(result)
            cnt += 1
        return

    for i in range(1, 7):
        result.append(i)
        path(x + 1, visited)
        result.pop()

cnt = 0
result = []
visited = [0] * 7
path(0, visited)

print(cnt)