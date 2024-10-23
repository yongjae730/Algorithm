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

# def findSum(numbers, queries):
#     # Write your code here
#     a = [0]
#     b = [0]
#     for x in numbers:
#         a.append(a[-1] + x)
#         b.append(b[-1] + (x == 0))
#     return [a[r] - a[l - 1] + x * (b[r] - b[l - 1]) for l, r, x in queries]
#
#
# if __name__ == '__main__':
#
#     numbers_count = int(input().strip())
#
#     numbers = []
#
#     for _ in range(numbers_count):
#         numbers_item = int(input().strip())
#         numbers.append(numbers_item)
#
#     queries_rows = int(input().strip())
#     queries_columns = int(input().strip())
#
#     queries = []
#
#     for _ in range(queries_rows):
#         queries.append(list(map(int, input().rstrip().split())))
#
#     result = findSum(numbers, queries)
#
#     print('\n'.join(map(str, result)))
#########################################################################################

# def getMaxArea(w, h, isVertical, distance):
#     result = []
#     width = [0,w]
#     height = [0,h]
#     if isVertical[0] == 0 and isVertical[1] == 0:
#         height[1] = distance[0]
#         a = (width[1]-width[0])*(height[1]-height[0])
#         height[0] = distance[1]
#         b = (width[1]-width[0])*(height[1]-height[0])
#     elif isVertical[0] == 0 and isVertical[1] == 1:
#         height[0] = distance[1]
#         a = (width[1]-width[0])*(height[1]-height[0])
#         width[0] = distance[1]
#         b = (width[1]-width[0])*(height[1]-height[0])
#
#     elif isVertical[0] == 1 and isVertical[1] == 0 :
#         width[0] = distance[0]
#         a = (width[1]-width[0])*(height[1]-height[0])
#         height[1] = distance[0]
#         b = (width[1]-width[0])*(height[1]-height[0])
#
#     elif isVertical[0] == 1 and isVertical[1] == 1:
#         width[0] = distance[0]
#         a = (width[1]-width[0])*(height[1]-height[0])
#         width[1] = distance[1]
#         b = (width[1]-width[0])*(height[1]-height[0])
#
#     result.append(a)
#     result.append(b)
#
#
#     return result

def sortedSum(a):

    result = 0
    b = [a[0]]
    i = 1
    while i <= len(a):
        b.sort()

        if i == len(a):
            for k in range(len(b)):
                result += b[k] * (k + 1)
            break
        for j in range(len(b)):
            result += b[j]*(j+1)

        result = result % 1000000007
        b.append(a[i])

        i+=1

    return result

a = []
for _ in range(3):
    a.append(int(input()))
print(sortedSum(a))
























