# heapq 우선순위 큐
from heapq import heappush,heappop

hq = []

# 삽입 (우선 순위에 따라서 더 큰 요소가 앞으로..)
heappush(hq,10)
heappush(hq,1)
heappush(hq,5)
heappush(hq,3)
# 삭제 (가장 우선순위가 높은 것이 반환)
x = heappop(hq)
print(x)

x = heappop(hq)
print(x)

x = heappop(hq)
print(x)

x = heappop(hq)
print(x)