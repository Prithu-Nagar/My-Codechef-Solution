import sys
from sys import stdin
from sys import stdout
try:
    test=sys.stdin.readline()
    test=int(test)
    for z in range(test):
        x=int(input())
        print(0,x)
except EOFError:
    pass