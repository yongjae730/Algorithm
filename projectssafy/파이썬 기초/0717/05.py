number_of_people = 0
number_of_book = 100

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def increase_user():
    global number_of_people
    number_of_people += 1

def decrease_book(ssafy):
    global number_of_book
    number_of_book = number_of_book - ssafy
    # number_of_book -= number
    print(f'남은 책의 수 : {number_of_book}')

def create_user(name, age, address):
    increase_user()
    print(f'{name}님 환영합니다!')
    user_info = {}
    user_info['name'] = name
    user_info['age'] = age
    user_info['address'] = address
    return user_info

many_user = list(map(create_user, name, age, address))

# 기존 회원 정보(many_user)에서 이름과 몇권 빌릴지 계산해서 새로운 회원 정보 딕셔너리를 반환하는 함수(람다로 변경할 함수)
def get_user(user):
    user_dict = {
        'name': user['name'],
        'number_of_rental_books': user['age'] // 10
    }
    return user_dict

def rental_book(info):
    decrease_book(info['number_of_rental_books'])
    print(f'{info["name"]}가 {info["number_of_rental_books"]}을 대여했습니다.')

# 람다 X 버전
print(list(map(get_user, many_user)))
list(map(rental_book, list(map(get_user, many_user))))

# 람다 O 버전
list(
    map(
        rental_book, 
        list(map(lambda user: {'name': user['name'], 'number_of_rental_books': user['age'] // 10}, many_user))
    )
)


