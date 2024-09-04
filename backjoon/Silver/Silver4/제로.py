K = int(input())
stack = []
result = 0
for i in range(K):
    N = int(input())
    if N != 0:
        stack.append(N)

    else:
        stack.pop()

while stack:
    result += stack.pop()
print(result)