import sys
from sys import stdin
try:
    x=12345
    while(x):
        a=input()
        if a=='42':
            break
        else:
            print(a)
except EOFError:
    pass