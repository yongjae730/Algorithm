# n = int(input())  # 분해합을 입력값으로 받음
#
# for i in range(1, n+1):   # 해당 분해합의 생성자 찾기
#     num = sum((map(int, str(i))))  # i의 각 자릿수를 더함
#     num_sum = i + num  # 분해합 = 생성자 + 각 자릿수의 합
#     # i가 작은 수부터 차례로 들어가므로 처음으로 분해합과 입력값이 같을때가 가장 작은 생성자를 가짐
#     if num_sum == n:
#         print(i)
#         break
# else:
#     print(0)

N = int(input())

for i in range(1, N+1): # 생성자의 범위는 분해합을 넘을 수 없기에 범위설정을 n+1까지 함
    number = sum((map(int, str(i)))) # 각 자리수를 분해해서 더해줌
    sum_number = i + number # 자릿수의 합과 i를 더해서 sum_num을 구함

    if sum_number == N: # 생성자가 발견되면 가장 작은 생성자를 찾는 문제기에 i를 출력한 후 break
        print(i)
        break
else:
	print(0)