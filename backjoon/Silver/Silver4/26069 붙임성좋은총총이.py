import sys

n = int(input())
dance_person = ['ChongChong']

for i in range(n):
    a,b = map(str,sys.stdin.readline().split())
    if a in dance_person and b not in dance_person:
        dance_person.append(b)
    elif b in dance_person and a not in dance_person:
        dance_person.append(a)
    
print(len(dance_person))

