def dfs(x, y, count):
    global ans
    ans = max(ans, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and not alphabet[nx][ny] in check_set:
            check_set.add(alphabet[nx][ny])
            dfs(nx, ny, count+1)
            check_set.remove(alphabet[nx][ny])



r, c = map(int, input().split())
alphabet = []
for _ in range(r):
    alphabet.append(list(input()))
ans = 0
check_set = set()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

check_set.add(alphabet[0][0])
dfs(0, 0, 1)
print(ans)