import sys

sys.stdin = open('input.txt')

# [입력]
#
# 첫 번째 줄에 테스트 케이스의 수 TC가 주어진다.
# 이후 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다.
T = int(input())
for tc in range(1, T + 1):
    # 각 테스트 케이스는 다음과 같이 구성되었다.
    # 1. 첫 번째 정수는 테스트에서 눌러야 하는 버튼의 개수 N 이다. (1 <= N <= 100)
    # 2. 이후 버튼 N개가 공백으로 구분되어 한 줄에 주어진다.
    # 버튼이 “O x” 의 형태이면 오렌지가 버튼 x를 눌러야 하며,
    # “B x”의 형태이면 블루가 버튼 x를 눌러야 한다. (1 <= x <= 100)
    # 문법을 모른다! (무식하게 입력을 잘 받아서 처리!)
    text = input().split()  # "4 B 2 O 1 O 2 B 4"
    N = int(text[0])

    # 작업목록 works 리스트로 해당 작업쌍
    works = []
    for i in range(1, len(text), 2):
        color = text[i]
        pos = int(text[i + 1])
        works.append([color, pos])

    # 로직

    # 초기화 (전역변수, 로봇변수)
    # 현재 시간 time
    time = 0

    # 로봇현재 위치
    B_pos = 1
    O_pos = 1

    # 로봇이 이동해야할
    # 위치
    B_nxt = None
    O_nxt = None

    # 로봇이 행동을 하였는지 유무 체크
    B_act = False
    O_act = False

    # 로봇을 움직이며 시뮬레이션 진행
    # works 데이터를 순회하면서 다음 누를 버튼을 찾는다!
    for i in range(len(works)):
        # 버튼을 눌러야하는 로봇과 그 버튼의 위치 값
        color, pos = works[i]
        # 해당 로봇 O와 로봇 B에 대한 행동...!\
        # => 해당 로봇이 가야할 다음 위치를 알아야 이동!
        # 해당 로봇 O가 이동해야하는 다음 위치를 탐색!
        for j in range(i, len(works)):
            _color, _pos = works[j]
            if _color == 'O':
                # 다음에 가야할 위치가 _pos
                O_nxt = _pos
                break

        # 해당 로봇 B가 이동해야하는 다음 위치를 탐색!
        for j in range(i, len(works)):
            _color, _pos = works[j]
            if _color == 'B':
                # 다음에 가야할 위치가 _pos
                B_nxt = _pos
                break
        while True:
            # 로봇이 행동을 하였는지 유무 체크
            B_act = False
            O_act = False

            time += 1
            # 로봇 O 와 로봇 B를 행동시키기! (1초)
            # 로봇의 현재 위치가 내가 가야할 위치가 되도록 이동!
            # O 로봇 이동
            if O_pos > O_nxt:
                O_pos -= 1
                O_act = True
            elif O_pos < O_nxt:
                O_pos += 1
                O_act = True
            # B 로봇 이동
            if B_pos > B_nxt:
                B_pos -= 1
                B_act = True
            elif B_pos < B_nxt:
                B_pos += 1
                B_act = True

            # O 로봇이 버튼을 누르기
            if O_pos == O_nxt and color == 'O' and O_pos == pos and O_act == False:
                break

            # B 로봇이 버튼을 누르기
            if B_pos == B_nxt and color == 'B' and B_pos == pos and B_act == False:
                break

            # O 로봇이 아무것도 안하는 경우
            if O_pos == O_nxt:
                O_act = True
            # B 로봇이 아무것도 안하는 경우
            if B_pos == B_nxt:
                B_act = True
    print()
