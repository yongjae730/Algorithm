def paper(x):
    if x == 1:
        return 1
    if x == 2:
        return 3

    return paper(x-1)+ 2*paper(x-2)

T = int(input())

for tc in range(1,T+1):
    size = int(input())

    x = size //10

    print(paper(x))