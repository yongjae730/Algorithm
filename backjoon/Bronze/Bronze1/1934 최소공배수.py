import sys

t = int(sys.stdin.readline())

for i in range(t) :

    a,b = map(int,sys.stdin.readline().split())

    for j in range(max(a,b), (a*b)+1):
        
        if (j % a) == 0 and (j % b) == 0 :
            
            break
        
    print(j)




