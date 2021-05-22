import sys
from sys import stdin
try:
    test=sys.stdin.readline()
    test=int(test)
    for z in range(test):
        n,m,k=sys.stdin.readline().split()
        n,m,k=int(n),int(m),int(k)
        a=[] 
        for i in range(n):
            a.append([int(j) for j in input().split()])
        for i in range(n):
            sum=0
            for j in range(m):
                sum+=a[i][j]
                a[i][j]=sum
        for i in range(m):
            sum=0
            for j in range(n):
                sum+=a[j][i]
                a[j][i]=sum
        arr=[] 
        for i in range(n+1):
            c=[]
            for j in range(m+1):
                c.append(0)
            arr.append(c)
        for i in range(n+1):
            for j in range(m+1):
                if i==0 or j==0:
                    arr[i][j]=0
                else:
                    arr[i][j]=a[i-1][j-1]
        o=1
        co=0
        mi=min(m,n)
        ans=0
        while o<mi+1:
            i=o
            j=m
            while i<n+1:
                p=i-o+1
                q=j-o+1
                r=arr[i][j]-arr[p-1][j]-arr[i][q-1]+arr[p-1][q-1]
                if r//(o*o)<k:
                    i+=1
                else:
                    s=o
                    e=m
                    while s<=e:
                        mid=(s+e)//2
                        p=i-o+1
                        q=mid-o+1
                        r=arr[i][mid]-arr[p-1][mid]-arr[i][q-1]+arr[p-1][q-1]
                        if r//(o*o)<k:
                            s=mid+1
                        else:
                            ans=mid
                            e=mid-1
                    co+=m-ans+1
                    i+=1
            o+=1
        print(co)
except EOFError:
    pass