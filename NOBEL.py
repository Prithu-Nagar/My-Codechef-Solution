import sys
from sys import stdin
from sys import stdout
try:
    test=sys.stdin.readline()
    test=int(test)
    for z in range(test):
        n,m=map(int,sys.stdin.readline().split())
        a=list(map(int,sys.stdin.readline().strip().split()))
        s=set(a)
        if len(s)<m:
            sys.stdout.write("Yes\n")
        else:
            sys.stdout.write("No\n")
except EOFError:
    pass