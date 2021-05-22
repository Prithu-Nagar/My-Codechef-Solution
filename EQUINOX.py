import sys
from sys import stdin
try:
    test=int(input())
    for z in range(test):
        n,a,b=map(int,input().split())
        w=0
        r=0
        for i in range(n):
            s=input()
            if(s[0]=='E'or s[0]=='I' or s[0]=='N' or s[0]=='O' or s[0]=='Q' or s[0]=='U' or s[0]=='X'):
                w+=a
            else:
                r+=b
        if w>r:
            print("SARTHAK")
        elif w<r:
            print("ANURADHA")
        else:
            print("DRAW")
except EOFError:
    pass