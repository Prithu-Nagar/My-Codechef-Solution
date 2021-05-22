import sys
from sys import stdin
from sys import stdout
try:
    test=int(input())
    for z in range(test):
        n,x,k=input().split()
        n,x,k=int(n),int(x),int(k)
        a=(n+1)%k
        if x%k==0 or x%k==a:
            print("YES")
        else:
            print("NO")
except EOFError:
    pass