t=int(input())
while t>0:
    n=int(input())
    s=input()
    for i in range(0,len(s),4):
        if s[i:i+4]=='0000':
            print('a',end='')
        elif s[i:i+4]=='0001':
            print('b',end='')
        elif s[i:i+4]=='0010':
            print('c',end='')
        elif s[i:i+4]=='0011':
            print('d',end='')
        elif s[i:i+4]=='0100':
            print('e',end='')
        elif s[i:i+4]=='0101':
            print('f',end='')
        elif s[i:i+4]=='0110':
            print('g',end='')
        elif s[i:i+4]=='0111':
            print('h',end='')
        elif s[i:i+4]=='1000':
            print('i',end='')
        elif s[i:i+4]=='1001':
            print('j',end='')
        elif s[i:i+4]=='1010':
            print('k',end='')
        elif s[i:i+4]=='1011':
            print('l',end='')
        elif s[i:i+4]=='1100':
            print('m',end='')
        elif s[i:i+4]=='1101':
            print('n',end='')
        elif s[i:i+4]=='1110':
            print('o',end='')
        elif s[i:i+4]=='1111':
            print('p',end='')
    print()
    t=t-1