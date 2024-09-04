number_of_book = 100


def rental_book(name, number):
    decrease_book(number)
    print(f'{name}님이 {number}책을 대여하였습니다.')

def decrease_book(ssafy):
    global number_of_book
    number_of_book = number_of_book - ssafy
    # number_of_book -= number
    print(f'남은 책의 수 : {number_of_book}')

# decrease_book(10)
rental_book('harry', 10)