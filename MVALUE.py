import sys
from sys import stdin
try:
    test=sys.stdin.readline()
    test=int(test)
    for z in range(test):
        n=sys.stdin.readline()
        q=[]
        n=int(n)
        ans=0
        v=list(map(int,sys.stdin.readline().strip().split()))
        v.sort()
        a = v[0]
        b= v[1]
        ans1 = a*b + abs(a-b)
        x = v[-1]
        y = v[-2]
        ans2 = x*y +(x-y)
        ans = max(ans1,ans2)
        sys.stdout.write(str(ans))
        sys.stdout.write("\n")
except EOFError:
    pass