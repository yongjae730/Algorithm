T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[1])
    time = arr[0]
    cnt = 1
    for i in range(1, len(arr)):
        if time[1] <= arr[i][0]:
            time = arr[i]
            cnt += 1

    print(f'#{tc} {cnt}')

    # for i in range(len(arr)):
    #     if arr[i][0] < start_clock:
    #         start_clock = arr[i][0]
    #         working_hours = arr[i][1] - arr[i][0]
    #         work.append(arr[i])
    #     elif arr[i][0] == start_clock:
    #         if working_hours > arr[i][1] - arr[i][0]:
    #             start_clock = arr[i][0]
    #             working_hours = arr[i][1] - arr[i][0]
    #             work[0] = arr[i]
