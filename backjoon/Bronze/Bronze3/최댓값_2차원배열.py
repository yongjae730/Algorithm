import sys


lst = []
for i in range(9):
    # 리스트를 받고 2차원 배열로 만드는 for문
    lst_a = list(map(int,sys.stdin.readline().split()))
    lst.append(lst_a)

max_num = 0

# 최댓값을 찾는 법
for j in range(9):
    for k in range(9):
        if lst[j][k] > max_num:
            max_num = lst[j][k]


print(max_num)


#행,렬 출력
for l in range(9):
    for q in range(9):
        if lst[l][q] == max_num:
            print(l +1 , q+1)
    

'''
for j in range(9):
    for k in range(9):
        if lst[j][k] > max_num:
            max_num = lst[j][k]
            h = j
            b = k

print(max_num)
print(h+1,b+1) 
민성이가 알려준 방법으로 시간절약 측면에서
더 좋은방법이다. 
'''





# mx_lst = []
# # 최댓값이 얼만지 찾는 과정
# for j in range(9):
#     lst[j].sort()
#     mx_lst.append(lst[j][-1])


# for k in range(9):
#     for l in range(9):
#         lst[k][j].index(mx_lst[-1])

