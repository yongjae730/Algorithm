# 총 16개의 피스를 사용
# 킹 1 퀸 1 룩 1 비숍 2 나이트 2 폰 8

# 첫째 줄에서 주어진 순서대로 몇 개의 피스를 더하거나 빼야 되는지를 출력한다


# 체스 견본과 찾은 체스를 비교하는 방식을 사용함

# need_chess = []


chess = [1, 1, 2, 2, 2, 8]
find_chess = list(map(int,input().split()))


# for i in range(find_chess) :
#     for j in range(chess):
#         i = j - i

# print(need_chess)


# for i in find_chess :
#     for j in chess:
#         i = j - i

#         need_chess.append(i)

# print(list(need_chess))
# 리스트끼리 비교하니까 들어온 수를 1개의 리스트로 보고 chess의 0번 인덱스에 모두 비교

for i in range(6):
    print(chess[i] - find_chess[i], end = ' ')

# 구글링 해보니 chess 말의 리스트 자체가 짧아
# range가 정해져 있어 범위를 정하고
# 각 요소의 인덱스 값을 비교후 빼면 됐다...
