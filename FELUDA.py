import sys
from sys import stdin
from sys import stdout
try:
    test=sys.stdin.readline()
    test=int(test)
    for z in range(test):
        counter=0
        s1=input()
        s2=input()
        if len(s1)>len(s2):
            sys.stdout.write("NO\n")
        else:
            for i in s1:
                if s1.count(i)<=s2.count(i):
                    counter+=1
                else:
                    break
            if(counter==len(s1)):
                sys.stdout.write("YES\n")
            else:
                sys.stdout.write("NO\n")
except EOFError:
    pass