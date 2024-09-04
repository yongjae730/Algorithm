'''
킹냥은 킹덤 왕국을 다스리는 유능한 왕이다.
문득 킹냥은 왕국 내 마을 중에서 인구 수가 많은 마을과 적은 마을의 인구 수 차이를 알고
싶다고 한다.
각 마을의 인구가 리스트로 주어질 때, 마을의 최대 인구 수와 최소 인구 수의 차이를
반환하는 population_difference 함수를 완성하시오.
왕국내 마을은 인구 수가 0명인 유령 마을도 존재한다고 하며 유령 마을도 인구 수
리스트에 포함되어 있다고 한다.
마을 인구 수 조사 리스트에는 적어도 2개의 마을은 포함되어 있다.
Python 내장함수 min, max, sorted (sort 메서드 포함) 사용 시 감점
'''



############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 min, max, sorted 함수 리스트 메서드 sort 를 사용하지 않습니다.
def population_difference(population_list):
    mx = population_list[0] 
    mn = population_list[0] #최댓값과 최소값에 각각 list의 첫 번째 인자로 할당
    for population in population_list:
        #최댓값을 구하는 함수
        if population > mx:
            # 만약 인구가 할당된 최댓값보다 크다면 그 값으로 교체
            mx = population 
    
    for population1 in population_list:
        #최소값을 구하는 함수
        if population1 < mn:
            #만약 인구가 할당된 최소값보다 작다면 그 값으로 교체
            mn = population1
    
    return mx-mn

    

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(population_difference([100, 200, 300, 400, 500]))  # 400
print(population_difference([50, 150, 250]))  # 200
print(population_difference([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]))  # 90
#####################################################
