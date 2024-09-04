a = int(input())

for i in range(a):
    b,c = input().split()
    for x in range(len(c)):
        print(c[x]*int(b), end = '')
    print()
