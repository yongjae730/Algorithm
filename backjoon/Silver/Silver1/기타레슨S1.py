def counter(mid):
    cnt = 1
    sum_lesson = 0
    for i in range(N):
        if sum_lesson + lessons[i] > mid:
            cnt += 1
            sum_lesson = lessons[i]
        else:
            sum_lesson += lessons[i]

    return cnt


def search(lessons, M):
    start = max(lessons)
    end = sum(lessons)
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        cnt = counter(mid)
        if cnt <= M:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1


    return ans

N, M = map(int, input().split())
lessons = list(map(int, input().split()))
result = search(lessons, M)
print(result)
