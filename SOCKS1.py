import sys
from sys import stdin
try:
    a,b,c=sys.stdin.readline().split()
    a,b,c=int(a),int(b),int(c)
    if a==b or a==c or b==c:
        print("YES")
    else:
        print("NO")
except EOFError:
    pass