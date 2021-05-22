import sys
from sys import stdin
try:
    test=sys.stdin.readline()
    test=int(test)
    for z in range(test):
        n=sys.stdin.readline()
        n=int(n)
        a=list(map(int,input().strip().split()))
        for i in range(n):
            c=0
            for j in range(i-1,-1,-1):
                if a[j]>a[i]:
                    break
                elif a[j]==a[i]:
                    c+=1
            for j in range(i+1,n):
                if a[j]>a[i]:
                    break
                elif a[j]==a[i]:
                    c+=1
            print(c,end=" ")
except EOFError:
    pass