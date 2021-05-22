try:
    a,o,c=map(int,input().split())
    x=20-o
    y=x*36
    m=c+y
    if(m>a):
        print("YES")
    else:
        print("NO")
except EOFError:
    pass