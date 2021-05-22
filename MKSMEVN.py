import sys
from sys import stdin
try:
    test=sys.stdin.readline()
    test=int(test)
    for z in range(test):
        n=sys.stdin.readline()
        n=int(n)
        a=list(map(int,input().strip().split()))
        sum=0
        for i in a:
            sum+=i
        if sum%2==0:
            print(0)
        else:
            ans=0
            for i in range(n):
                if(a[i]%2==0) and (a[i]+1)//2-1 <=0:
                    ans=1
                    break
            if ans==0:
                print(-1)
            else:
                print(1)
except EOFError:
    pass