import sys

sys.stdin = open('input.txt', 'r')

'''
0 : 상
1 : 하
2 : 좌
3 : 우
'''
dx = [0, 0, -1, 1]  # 좌표상의 상하좌우 이기 때문에 2차원 배열이랑 다름
dy = [1, -1, 0, 0]
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    atoms = []
    power = 0
    for _ in range(N):
        x, y, direction, energy = map(int, input().split())
        x = (x + 1000) * 2
        y = (y + 1000) * 2

        atoms.append([x, y, direction, energy])

    while atoms:
        next_location = []
        collapse_location = set()
        next_atom_info = []

        for i in range(len(atoms)):
            x, y, direction, energy = atoms[i]
            nx, ny = x + dx[direction], y + dy[direction]
            if 0 <= nx < 4000 and 0 <= ny < 4000:
                if (nx, ny) in next_location:
                    collapse_location.add((nx, ny))
                else:
                    next_location.append((nx, ny))
                next_atom_info.append([nx, ny, direction, energy])
        # 에너지
        atoms = []

        for j in range(len(next_atom_info)):
            x, y, direction, energy = next_atom_info[j]

            if (x, y) in collapse_location:
                power += energy
            else:
                atoms.append([x, y, direction, energy])

    print(f'#{tc} {power}')
