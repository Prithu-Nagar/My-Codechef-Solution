import sys
from sys import stdin
try:
    test=sys.stdin.readline()
    test=int(test)
    for z in range(test):
        n,w,wr=input().split()
        n,w,wr=int(n),int(w),int(wr)
        a=list(map(int,input().strip().split()))
        m=[0]*max(a)
        for i in a:
            m[i-1]+=1
        if wr>=w:
            print("YES")
        else:
            w-=wr
            for i in range(n):
                if m[a[i]-1]>=2:
                    c=m[a[i]-1]
                    if c%2==0:
                        w-=c*a[i]
                    else:
                        w-=(c-1)*a[i]
                    m[a[i]-1]=0
                if w<=0:
                    break
            if w<=0:
                print("YES")
            else:
                print("NO")
except EOFError:
    pass