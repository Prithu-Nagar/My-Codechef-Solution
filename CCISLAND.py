import sys
from sys import stdin
from sys import stdout
try:
    test=sys.stdin.readline()
    test=int(test)
    for z in range(test):
        x,y,a,b,d=sys.stdin.readline().split()
        x,y,a,b,d=int(x),int(y),int(a),int(b),int(d)
        a*=d
        b*=d
        if x-a>=0 and y-b>=0:
            sys.stdout.write('YES\n')
        else:
            sys.stdout.write('NO\n')
except EOFError:
    pass