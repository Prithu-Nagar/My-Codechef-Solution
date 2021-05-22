import sys
from sys import stdin
try:
    test=sys.stdin.readline()
    test=int(test)
    for z in range(test):
        n=sys.stdin.readline()
        n=int(n)
        a=0
        if n>4:
            i=n//4
            a=44*i
            n%=4
            a+=4*(4-n)
        if n==1:
            a+=20
        if n==2:
            a+=36
        if n==3:
            a+=51
        if n==4:
            a+=60
        print(a)
except EOFError:
    pass