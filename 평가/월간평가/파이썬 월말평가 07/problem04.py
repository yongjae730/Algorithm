'''
보물 사냥꾼 괴도냥은 세상을 돌아다니며 다양한 보물을 수집하고 있다.
❖ 괴도냥은 문득 수집한 보물의 총 값어치가 궁금하여 총가격을 계산해보기로 했다.
❖ 수집한 보물이 리스트로 주어지고, 보물의 가격이 딕셔너리로 주어질 때 보물의 총 가격을
반환하는 calculate_total_value 함수를 완성하시오.
❖ 만약 보물을 한개도 얻지 못한 경우 총 가격은 0원이다
'''

# 보물의 가격 표
treasure_prices = {
    "gold": 100,
    "silver": 50,
    "diamond": 200,
    "ruby": 150,
    "emerald": 120,
    "sapphire": 180,
    "pearl": 80,
    "coin": 1
}

############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def calculate_total_value(treasure_list):
    total_price = 0
    for i in treasure_list: # 입력을 받은 보석을 순회
        for j in treasure_prices: # 보물의 가격표를 순회
            if i == j: #보물과 보석을 서로 비교
                total_price += treasure_prices[j] # 보석의 가격을 total_price에 더해준다.
    return total_price
            

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(calculate_total_value(["gold", "silver", "diamond", "gold", "silver"]))  # 500
print(calculate_total_value(["pearl"]))  # 80
#####################################################
