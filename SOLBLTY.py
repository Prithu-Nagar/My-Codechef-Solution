import sys
from sys import stdin
try:
    test=sys.stdin.readline()
    test=int(test)
    for z in range(test):
        n,x,y=input().split()
        n,x,y=int(n),int(x),int(y)
        s=x+(100-n)*y
        print(s*10)
except EOFError:
    pass