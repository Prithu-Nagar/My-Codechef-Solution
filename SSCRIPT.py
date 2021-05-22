import sys
from sys import stdin
try:
    test=sys.stdin.readline()
    test=int(test)
    for z in range(test):
        n,k=sys.stdin.readline().split()
        n,k=int(n),int(k)
        a=list(input().split())
        c,flag=0,0
        for i in a[0]:
            if i=='*':
                c+=1
                if c==k:
                    print("YES")
                    flag+=1
                    break
            else:
                c=0
        if flag==0:
            print("NO")
except EOFError:
    pass