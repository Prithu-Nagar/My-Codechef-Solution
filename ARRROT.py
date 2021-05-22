import sys
from sys import stdin
try:
    n=int(input())
    a=list(map(int,input().strip().split()))
    q=int(input())
    x=list(map(int,input().strip().split()))
    m=10**9+7
    summer=0
    for i in a:
        summer=(summer+i+m)%m
    for i in range(q):
        summer=(2*summer)%m
        print(summer)
except EOFError:
    pass