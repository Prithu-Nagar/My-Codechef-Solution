import sys
from sys import stdin
try:
    test=sys.stdin.readline()
    test=int(test)
    for z in range(test):
        n=sys.stdin.readline()
        if '7' in n:
            print("True")
        else:
            print("False")
except EOFError:
    pass