n,h,x=input().split()
n,h,x=int(n),int(h),int(x)
a=list(map(int,input().strip().split()))
a.sort()
if a[-1]+x>=h:
    print("YES")
else:
    print("NO")