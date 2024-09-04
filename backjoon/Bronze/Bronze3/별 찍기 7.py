# n = int(input())

# for i in range(1,n+1):
#     print(' '*i+'*'*(2*i-1))

# 들어온 범위 만큼의 별을 찍어주기 위해 해당 코드를 짰으나
# *i만큼의 공백을 주니 별이 점점 뒤로 밀림
# 해결하기 위해 숫자가 점점 줄어들어야 한다는 사실을 깨닫고
# input  n 을 활용해 아래 코드 작성

n = int(input())

for i in range(1, n+1):
    print(' '*(n-i)+'*'*(2*i-1))

# 별을 뒤집어 출력하기 위해 range 마지막에 step 요소인 항목에 -1 을 넣었으나 출력이 안됨

# for i in range(0, n-1,-1):
#     print(' '*(n-i)+'*'*(2*i-1))

for i in range(n-1, 0,-1):
    print(' '*(n-i)+'*'*(2*i-1))

# range 시작이 꼭 0부터 할 이유는 없다고 생각해 뒤집으니 정상적으로 출력 됨