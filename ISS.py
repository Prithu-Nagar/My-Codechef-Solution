import sys
from sys import stdin
from sys import stdout
try:
    n=4000005
    a=[0]*n
    b=list(range(n))
    for i in range(2,n):
        if b[i]==i:
            b[i]=i-1
            j=2*i
            while j<n:
                b[j]=(b[j]//i)*(i-1)
                j+=i
    for i in range(1,n):
        a[i]+=i-1
        j=2*i
        while j<n:
            a[j]+=i*((1+b[j//i])//2)
            j+=i
    test=sys.stdin.readline()
    test=int(test)
    for z in range(test):
        k=sys.stdin.readline()
        k=int(k)
        sys.stdout.write(str(a[4*k+1])+"\n")
except EOFError:
    pass