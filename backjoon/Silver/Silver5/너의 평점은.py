# grade = 0
# while True:
#     a, b, c = map(str, input().split())
#     num = 0


#     if c == 'A+':
#         grade += 4.5
#         num += 1
#     if c == 'A0':
#         grade += 4.0
#         num += 1
#     if c == 'B+':
#         grade += 3.5
#         num += 1
#     if c == 'B0':
#         grade += 3.0
#         num += 1
#     if c == 'C+':
#         grade += 2.5
#         num += 1
#     if c == 'C0':
#         grade += 2.0
#         num += 1
#     if c == 'D+':
#         grade += 1.5
#         num += 1
#     if c == 'D0':
#         grade += 1.0
#         num += 1
#     if c == 'F':    
#         grade += 0
#         num += 1
#     if c == 'P':
#         num += 1
        
    
#     average = (grade / num)
#     print(average)
#     False
# 처음에 입력수가 무한인줄알고 입력 받으면 받는대로 점수 계산을 하려했으나
# 입력수도 한정되어있고 짠 코드가 1회성이라는걸 깨달음

grade = {'A+': 4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0}



total = 0
sum_score = 0
average = 0
for i in range(20):
    a, b, c = map(str,input().split())
    if c == 'P':
        continue
    
    total += float(b)*grade[c]   #float을 쓰지 않으면 b(학점)이 문자열이라 연산이 안됨 
    sum_score += float(b)       # 처음엔 그냥 학점 다 더했는데 그러면 오류떠서 sum_score이라는 변수 만들어줌

print(round(total/sum_score, 6))


