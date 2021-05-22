import sys
from sys import stdin
from sys import stdout
try:
    test=sys.stdin.readline()
    test=int(test)
    for z in range(test):
        l=list(map(int,sys.stdin.readline().strip().split()))
        x=sys.stdin.readline()
        x=int(x)
        for i in range(9,-1,-1):
            if l[i]<=x:
                x-=l[i]
            else:
                break
        sys.stdout.write(str(i+1)+"\n")
except EOFError:
    pass