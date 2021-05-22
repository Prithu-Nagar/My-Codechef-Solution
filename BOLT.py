import sys
from sys import stdin
try:
    test=sys.stdin.readline()
    test=int(test)
    for z in range(test):
        k1,k2,k3,v=sys.stdin.readline().split()
        k1,k2,k3,v=float(k1),float(k2),float(k3),float(v)
        x=k1*k2*k3*v
        y=100/x
        if round(y, 2)<9.58:
            print("YES")
        else:
            print("NO")
except EOFError:
    pass