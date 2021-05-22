import sys
from sys import stdin
from sys import stdout
try:
    test=sys.stdin.readline()
    test=int(test)
    for z in range(test):
        n,m=sys.stdin.readline().split()
        n,m=int(n),int(m)
        c=0
        s=[1]*(n+1)
        for i in range(2,n+1):
            a=m%i
            c+=s[a]
            for j in range(a,n+1,i):
                s[j]+=1
        sys.stdout.write(str(c)+"\n")
except EOFError:
    pass