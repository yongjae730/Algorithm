'''
킹냥은 킹덤 왕국을 다스리는 유능한 왕이다.
문득 킹냥은 왕국 내 모든 마을의 평균 인구 수가 궁금하다고 한다.
각 마을의 인구 수가 리스트로 주어질 때, 왕국의 평균 인구 수를 반환하는
average_population 함수를 완성하시오.
왕국내 마을은 인구 수가 0명인 유령 마을도 존재한다고 하며 유령 마을도 인구 수
리스트에 포함되어 있다고 한다.
마을 인구 수 조사 리스트에는 적어도 2개의 마을은 포함되어 있다.
average_population 함수의 반환 값은 실수(float) 타입이다.
❖ython 내장함수 len, sum 사용 시 감점

'''

############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 sum, len 함수를 사용하지 않습니다.
def average_population(population_list):
    total_population = 0   # 더한 모든 인구수를 저장할 변수
    cnt = 0 #몇 개의 마을인지 센다
    for population in population_list:
        total_population += population   #population_list를 순회하면서 인구수를 다 더한다
        cnt += 1
    return total_population/cnt  




# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(average_population([1000, 2000, 3000, 4000, 5000]))   # 3000.0
print(average_population([1500, 2500, 3500]))               # 2500.0
print(average_population([1234, 5678, 91011]))              # 32641.0
#####################################################