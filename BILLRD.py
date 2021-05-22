try:
    t = int(input())
    while t>0:
        n,noc,x,y=input().split()
        n,noc,x,y=int(n),int(noc),int(x),int(y)
        board=[]
        points=[]
        if x == y:
            print(n,n)
        else:
            if x < y:
                board = [(x+n-y,n),(n,n-y+x),(y-x,0),(0,y-x)]
            else:
                board = [(n,y+n-x),(y+n-x,n),(0,x-y),(x-y,0)]
            points = board[(noc-1) % 4]
            print(points[0],points[1])
        t-=1
except EOFError:
    pass