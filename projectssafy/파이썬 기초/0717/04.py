number_of_people = 0


def increase_user():
    pass


def create_user(name, age, address):
    increase_user()
    print(f'{name}님 환영합니다!')
    user_info = {}
    user_info['name'] = name
    user_info['age'] = age
    user_info['address'] = address
    return user_info


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

# 풀이 1
many_user = list(map(create_user, name, age, address))
print(many_user)

# 풀이 2
many_user = []
for name, age, address in zip(name, age, address):
    many_user.append(create_user(name, age, address))
print(many_user)