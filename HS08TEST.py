import sys
from sys import stdin
try:
    n,b=sys.stdin.readline().split()
    n,b=int(n),float(b)
    if n%5==0 and b-n>=0.5:
        print('%.2f'%(b-n-0.5))
    else:
        print('%.2f'%b)
except EOFError:
    pass