import sys
from sys import stdin
try:
    test=sys.stdin.readline()
    test=int(test)
    for z in range(test):
        r,c,x=sys.stdin.readline().split()
        r,c,x=int(r),int(c),int(x)
        flag=0
        diff=0
        a=[]
        b=[]
        for i in range(r):
            p =[] 
            p=list(map(int,input().strip().split()))
            a.append(p)
        for i in range(r):
            q =[]
            q=list(map(int,input().strip().split()))
            b.append(q)
        if r<x and c<x:
            for i in range(r):
                for j in range(c):
                    if a[i][j]==b[i][j]:
                        continue
                    else:
                        flag=1
                        break
            if flag==1:
                print("No")
            else:
                print("Yes")
        elif r<x:
            for i in range(r):
                for j in range(c-x+1):
                    if a[i][j]!=b[i][j]:
                        diff=b[i][j]-a[i][j]
                        for k in range(j+1,j+x+1):
                            a[i][k]+=diff
            for i in range(r):
                for j in range(c):
                    if a[i][j]==b[i][j]:
                        continue
                    else:
                        flag=1
                        break
            if flag==1:
                print("No")
            else:
                print("Yes")
        elif c<x:
            for i in range(c):
                for j in range(r-x+1):
                    if a[j][i]!=b[j][i]:
                        diff=b[j][i] - a[j][i]
                        print(diff)
                        for k in range(j+1,j+x+1):
                            a[k][i]+=diff
            for i in range(r):
                for j in range(c):
                    if a[i][j]==b[i][j]:
                        continue
                    else:
                        flag=1
                        break
            if flag==1:
                print("No")
            else:
                print("Yes")
        elif r>=x and c>=x:
            for i in range(r):
                for j in range(c-x+1):
                    if a[i][j]!=b[i][j]:
                        diff=b[i][j]-a[i][j]
                        for k in range(j,j+x):
                            a[i][k]+=diff
            for i in range(c):
                for j in range(r-x+1):
                    if a[j][i]!=b[j][i]:
                        diff=b[j][i] - a[j][i]
                        for k in range(j,j+x):
                            a[k][i]+=diff
            for i in range(r):
                for j in range(c):
                    if a[i][j]==b[i][j]:
                        continue
                    else:
                        flag=1
                        break
            if flag==1:
                print("No")
            else:
                print("Yes")
except EOFError:
    pass