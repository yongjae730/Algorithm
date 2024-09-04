number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1


# 고객정보를 딕셔너리로 반환하는 함수
def create_user(name, age, address):
    increase_user()
    print(f'{name}님 환영합니다!')
    # 풀이 1
    user_info = {}
    user_info['name'] = name
    user_info['age'] = age
    user_info['address'] = address

    # 풀이 2
    # user_info = {
    #     'name': name,
    #     'age': age,
    #     'address': address
    # }
    return user_info

print(f'현재 가입된 유저 수 : {number_of_people}')
result = create_user('홍길동', 30, '서울')
print(result)  # {'name': '홍길동', 'age': 30, 'address': '서울'}
print(f'현재 가입된 유저 수 : {number_of_people}')