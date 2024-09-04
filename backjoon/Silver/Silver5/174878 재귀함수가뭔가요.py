'''
어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.
"재귀함수가 뭔가요?"                                                       # n만큼 반복시켜야함  
"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어. # n만큼 반복시켜야함
마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."

"재귀함수가 뭔가요?"
________"재귀함수는 자기 자신을 호출하는 함수라네" # n만큼 반복 시켜야함
________라고 답변하였지.                         # n만큼 반복 시켜야함

'''


# a = int(input())

# def professor(a):

#     if a == 0:
#         print('"재귀 함수는 자기 자신을 호출하는 함수라네"')
#     else:
#         print('"재귀함수가 뭔가요?"')
#         print('"잘 들어보게. 옛날옛날 한 산 꼭대기에 이 세상 모든 지식을 통달한 선인이 있었어.')
#         print('마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
#         print('그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        
#         a -= -1
              
#         return 

# result = professor(a)
# -> 이렇게 하면 앞의 _ 가 존재할 수 없다는 사실을 알았음 별도의 카운트를 써야함.


a = int(input())

print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')

def professor(a, cnt):
    print('____'*cnt + '"재귀함수가 뭔가요?"')
    if a == cnt:
        print('____'*cnt+'"재귀함수는 자기 자신을 호출하는 함수라네"')
    else:
        print('____'*cnt + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        print('____'*cnt + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
        print('____'*cnt + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        
        professor(a , cnt+1)
    
    print('____'*cnt+'라고 답변하였지.')

professor(a,0)

