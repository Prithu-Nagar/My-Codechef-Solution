def ttt(b):
    cx,co=0,0
    n=0
    for i in range(3):
        for j in range(3):
            if b[i][j]=="X":
                cx+=1
            elif b[i][j]=="O":
                co+=1
            elif b[i][j]=="_":
                n+=1
    x,o=0,0
    if b[0][0]==b[1][1]==b[2][2]=="X" or b[0][2]==b[1][1]==b[2][0]=="X" or b[0][2]==b[1][2]==b[2][2]=="X" or b[0][1]==b[1][1]==b[2][1]=="X" or b[0][0]==b[1][0]==b[2][0]=="X" or b[0][0]==b[0][1]==b[0][2]=="X" or b[1][0]==b[1][1]==b[1][2]=="X" or  b[2][0]==b[2][1]==b[2][2]=="X":
        x=1
    if b[0][0]==b[1][1]==b[2][2]=="O" or b[0][2]==b[1][1]==b[2][0]=="O" or b[0][2]==b[1][2]==b[2][2]=="O" or b[0][1]==b[1][1]==b[2][1]=="O" or b[0][0]==b[1][0]==b[2][0]=="O" or b[0][0]==b[0][1]==b[0][2]=="O" or b[1][0]==b[1][1]==b[1][2]=="O" or  b[2][0]==b[2][1]==b[2][2]=="O":
        o=1
    if (x==1 and o==1) or (cx-co<0) or (cx-co>1):
        return 3
    elif (cx==0 and co==0 and n==9) or (x==0 and o==0 and n>0):
        return 2
    elif (x==1 and o==0 and cx>co) or (x==0 and o==1 and cx==co) or (x==0 and o==0 and n==0):
        return 1
    return 3
test=input()
test=int(test)
for z in range(test):
    b=[]
    for i in range(3):
        c=list(input())
        b.append(c)
    print(ttt(b))