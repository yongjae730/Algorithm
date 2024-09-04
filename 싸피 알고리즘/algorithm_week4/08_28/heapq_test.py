# # 파이썬에서는 heapq 라이브러리를 통해서
# # heapify 한 상태로 유지가 되도록 리스트(배열)를 만든다.
# from heapq import heapify, heappop, heappush
#
#
# #
# # hq = []
# #
# # # 힙 삽입 연산
# # heappush(hq, 1)
# # heappush(hq, 2)
# # heappush(hq, 3)
# # heappush(hq, 4)
# # heappush(hq, 5)
# # heappush(hq, 6)
# #
# # print(hq)
# #
# # x = heappop(hq)
# # print(x)
# # x = heappop(hq)
# # print(x)
# # x = heappop(hq)
# # print(x)
# # x = heappop(hq)
# # print(x)
# # x = heappop(hq)
# # print(x)
# #
#
# class Heap():
#     def __init__(self, key=lambda x: x):
#         self.hq = []
#         self.key = key
#
#     def push(self, x):
#         heappush(self.hq, (self.key(x), x))
#
#     def pop(self):
#         return heappop(self.hq)[1]
#
#     def __len__(self):
#         return len(self.hq)
#
#
# # 최소힙
# mnheap = Heap()
#
# mnheap.push(5)
# mnheap.push(1)
# mnheap.push(6)
# mnheap.push(8)
# mnheap.push(2)
# mnheap.push(0)
# x = mnheap.pop()
# print(x)
# x = mnheap.pop()
# print(x)
# x = mnheap.pop()
# print(x)
# x = mnheap.pop()
# print(x)
# x = mnheap.pop()
# print(x)
# x = mnheap.pop()
# print(x)
#
# mxheap = Heap(lambda x: -x)
#
# mxheap.push(5)
# mxheap.push(1)
# mxheap.push(6)
# mxheap.push(8)
# mxheap.push(2)
# mxheap.push(0)
# x = mxheap.pop()
# print(x)
# x = mxheap.pop()
# print(x)
# x = mxheap.pop()
# print(x)
# x = mxheap.pop()
# print(x)
# x = mxheap.pop()
# print(x)
# x = mxheap.pop()
# print(x)
#
# from functools import cmp_to_key
#
# def compare(x, y):
#     return x < y
#
# heap = Heap(key=cmp_to_key(compare))

lst = []
for _ in range(2):
    lst2 = []
    for _ in range(3):
        lst2.append(0)
    lst.append(lst2)
print(lst)
lst3 = [[0]*3]*2
print(lst3)