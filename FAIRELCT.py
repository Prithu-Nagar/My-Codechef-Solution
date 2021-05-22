try:
    t=int(input())
    while t>0:
        x,y=input().split()
        x,y=int(x),int(y)
        l1=list(map(int,input().strip().split()))
        l2=list(map(int,input().strip().split()))
        l1.sort()
        l2.sort()
        if sum(l1)>sum(l2):
            print('0')
            continue
        low=0
        high=y-1
        count=0
        while low<x and high>-1:
            l1[low],l2[high]=l2[high],l1[low]
            count+=1
            if sum(l1)>sum(l2):
                print(count)
                break
            low+=1
            high-=1
        if sum(l1)<=sum(l2):
            print('-1')
        t=t-1
except EOFError:
    pass