import sys
from sys import stdin
from sys import stdout
try:
    test=sys.stdin.readline()
    test=int(test)
    for z in range(test):
        m,h=map(int,sys.stdin.readline().strip().split())
        bmi=m//(h*h)
        if(bmi>=30):
            sys.stdout.write("4\n")
        elif(bmi<=29 and bmi>=25):
            sys.stdout.write("3\n")
        elif(bmi<=24 and bmi>=19):
            sys.stdout.write("2\n")
        elif(bmi<=18):
            sys.stdout.write("1\n")
except EOFError:
    pass