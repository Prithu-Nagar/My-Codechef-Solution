import sys
from sys import stdin
try:
    test=sys.stdin.readline()
    test=int(test)
    for z in range(test):
        w1,w2,x1,x2,m=sys.stdin.readline().split()
        w1,w2,x1,x2,m=int(w1),int(w2),int(x1),int(x2),int(m)
        if w2-w1>=x1*m and w2-w1<=x2*m:
            print(1)
        else:
            print(0)
except EOFError:
    pass