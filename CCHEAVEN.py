import sys
from sys import stdin
try:
    test=sys.stdin.readline()
    test=int(test)
    for z in range(test):
        n=int(input())
        a=input()
        s=list(a)
        c=0
        l=0
        flag=0
        if s.count('1')>=len(s)/2:
            print("YES")
        else:
            for i in s:
                if i=='0':
                    l+=1
                else:
                    c+=1
                    l+=1
                if c>=l/2:
                    flag=1
                    break
            if flag==1:
                print("YES")
            else:
                print("NO")
except EOFError:
    pass