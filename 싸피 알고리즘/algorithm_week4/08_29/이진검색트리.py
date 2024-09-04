import sys
sys.setrecursionlimit(10**9)

def tree(A):
    if len(A) == 0:
        return

    mid = A[0]
    left = []
    right = []

    for i in range(len(A)):
        if A[i] > mid:
            left += A[1:i]
            right += A[i:]
            break
    else:
        left += A[1:]

    tree(left)
    tree(right)
    print(A[0])


arr = []
while True:
    try:
        n = int(input())
        arr.append(n)
    except:
        break

tree(arr)
