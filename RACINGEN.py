import sys
from sys import stdin
try:
    test=sys.stdin.readline()
    test=int(test)
    for z in range(test):
        x,r,n=sys.stdin.readline().split()
        x,r,n=int(x),int(r),int(n)
        if x>=60*r:
            if r<=n:
                print("YES")
            else:
                print("NO")
        else:
            if x+2*(60*r-x)<=60*n:
                print("YES")
            else:
                print("NO")
except EOFError:
    pass