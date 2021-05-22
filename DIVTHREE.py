try:
    t=int(input())
    while t>0:
        count=0
        x,y,z=input().split()
        x,y,z=int(x),int(y),int(z)
        l=list(map(int,input().strip().split()))
        summer = sum(l)//y 
        if summer > z:
            print(z)
        else:
            print(summer)
        t=t-1
except EOFError:
    pass