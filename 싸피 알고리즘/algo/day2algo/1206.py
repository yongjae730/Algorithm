# 첫번째 +2칸 까지 높이 잼 (음수면 continue) 양수면 그 값을 가져간다.
# 역순으로 -2칸 까지 높이 잰다. (음수면 여전히 continue) 양수면 그 값을 가져간다(1번과 별도의 변수)
# 첫번째에서 구한 수와 두번째에서 구한 수를 빼준다.



Tc = 10

for i in range(1, 11):
    N = int(input())
    build = list(map(int, input().split()))
    sum_view = 0
    for j in range(2, N-2):
        lst = [build[j-2], build[j-1], build[j+1], build[j+2]]
        view = build[j] - max(lst)
        if view < 0 :
            continue
        if view > 0:
            sum_view += view

    print(f'#{i} {sum_view}')


