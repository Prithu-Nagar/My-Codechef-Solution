import sys
from sys import stdin
try:
    test=sys.stdin.readline()
    test=int(test)
    for z in range(test):
        n,s=sys.stdin.readline().split()
        n,s=int(n),int(s)
        x=n//s
        print(x)
except EOFError:
    pass