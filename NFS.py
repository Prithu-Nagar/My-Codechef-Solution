import sys
from sys import stdin
try:
    test=sys.stdin.readline()
    test=int(test)
    for z in range(test):
        u,v,a,s=sys.stdin.readline().split()
        u,v,a,s=int(u),int(v),int(a),int(s)
        if u<=v:
            print("Yes")
        else:
            if ((u*u) -(v*v)) <=(2*a*s):
                print("Yes")
            else:
                print("No")
except EOFError:
    pass