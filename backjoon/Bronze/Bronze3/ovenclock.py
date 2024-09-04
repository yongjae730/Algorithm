a, b , c = map(int,input().split())

if a == b == c :
    print(10000+a*1000)
else:
    if a==b or a == c :
        print (1000 + a*100 )
    if b == c :
        print (1000 + b*100)
    else:
        if a>b>c or a> c>b:
            print(a*100)
        if b>a>c or b>c>a :
            print(b*100)
        if c >b >a or c >a >b:
            print(c*100)