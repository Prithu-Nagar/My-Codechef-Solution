import sys
from sys import stdin
try:
    t=list(map(int,sys.stdin.readline().strip().split()))
    for z in range(t[0]):
        c=int(input())
        d=0
        temp=c
        while temp>0:
            temp//=2
            d+=1
        a=(2**(d-1))-1
        b=a^c
        print(a*b)
except EOFError:
    pass