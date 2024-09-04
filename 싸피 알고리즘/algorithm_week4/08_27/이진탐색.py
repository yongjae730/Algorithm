def in_order(node,i):
    global num
    if i == N:
        return
    in_order(left[node],i+1)
    in_order(right[node], i+1)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    left = [0] * (N + 1)
    right = [0] * (N + 1)
    num = [0] * (N + 1)

    in_order(1,1)
    print(num)