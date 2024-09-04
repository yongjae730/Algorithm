N = int(input())
paper = [[0 for _ in range(100)] for _ in range(100)]

for i in range(N):
    a, b = map(int, input().split())
    for x in range(a, a + 10):
        for y in range(b, b + 10):
            if paper[x][y] == 0:
                paper[x][y] = 1

cnt = 0
for i in range(100):
    cnt += sum(paper[i])

print(cnt)
