import sys
from sys import stdin
try:
    test=sys.stdin.readline()
    test=int(test)
    for z in range(test):
        a,y,x=sys.stdin.readline().split()
        a,y,x=int(a),int(y),int(x)
        if a>=y:
            print(x*y)
        else:
            print(x*a+1)
except EOFError:
    pass