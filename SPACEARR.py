import sys
from sys import stdin
try:
    test=list(map(int,sys.stdin.readline().strip().split()))
    for z in range(test[0]):
        n=list(map(int,sys.stdin.readline().strip().split()))
        a=list(map(int,sys.stdin.readline().strip().split()))
        a.sort()
        ans=0
        t=0
        for i in range(n[0]):
            if i+1<a[i]:
                t=1
                break
            ans+=i+1-a[i]
        if t==1:
            print("Second")
        else:
            if ans%2==1:
                print("First")
            else:
                print("Second")
except EOFError:
    pass