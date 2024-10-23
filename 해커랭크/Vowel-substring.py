#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findSubstring' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
# lst = ['a', 'e', 'i', 'o', 'u']
#
#
# def findSubstring(s, k):
#     # Write your code here
#     result = 0
#
#     ans = 'aeiou'
#
#     for i in range(len(s) - k):
#         cnt = 0
#         for j in range(i, i + k):
#             if s[j] in 'aeiou':
#                 cnt += 1
#
#         if cnt > result:
#             result = cnt
#             ans = s[i: i + k]
#
#     if ans == 'aeiou':
#         ans = 'Not found!'
#
#     return ans
# def findSubstring(s, k):
#     # Write your code here
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     result = 0
#     cnt = 0
#     for i in range(k):
#         if s[i] in vowels:
#             cnt += 1
#     result = cnt
#     ans = 0
#
#     for j in range(k,len(s)):
#         if s[j] in vowels:
#             cnt += 1
#         if s[j - k] in vowels:
#             cnt -= 1
#
#         if cnt > result:
#             result = cnt
#             ans = j - k + 1
#
#     if result > 0:
#         return s[ans: (ans + k)]
#
#     else:
#         return 'Not found!'
#
#
# s = 'eiuaooo'
# k = 4
# result = findSubstring(s, k)
# print(result)



#
# Complete the 'findSum' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY numbers
#  2. 2D_INTEGER_ARRAY queries
#

def findSum(numbers, queries):
    # Write your code here
    a = [0]
    b = [0]
    for x in numbers:
        a.append(a[-1] + x)
        b.append(b[-1] + (x == 0))
    return [a[r] - a[l - 1] + x * (b[r] - b[l - 1]) for l, r, x in queries]


if __name__ == '__main__':

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    queries_rows = int(input().strip())
    queries_columns = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(list(map(int, input().rstrip().split())))

    result = findSum(numbers, queries)

    print('\n'.join(map(str, result)))