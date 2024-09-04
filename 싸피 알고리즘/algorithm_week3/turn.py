'''
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 첫 줄에 N과 M이 주어지고, 다음 줄에 10억 이하의 자연수 N개가 주어진다. 3<=N<=20, N<=M<=1000,
'''
T= int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    number = list(map(int,input().split()))

    for i in range(M):
        A = number.pop(0)
        number.append(A)

    print(f'#{tc} {number[0]}')