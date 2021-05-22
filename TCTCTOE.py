import sys
from sys import stdin
try:
    def ttt(board):
        cx,co=0,0
        n=0
        for i in range(3):
            for j in range(3):
                if board[i][j]=="X":
                    cx+=1
                elif board[i][j]=="O":
                    co+=1
                elif board[i][j]=="_":
                    n+=1
        x,o=0,0
        if board[0][0]=="X" and board[1][1]=="X" and board[2][2]=="X":
            x=1
        elif board[0][2]=="X" and board[1][1]=="X" and board[2][0]=="X":
            x=1
        elif board[0][2]=="X" and board[1][2]=="X" and board[2][2]=="X":
            x=1
        elif board[0][1]=="X" and board[1][1]=="X" and board[2][1]=="X":
            x=1
        elif board[0][0]=="X" and board[1][0]=="X" and board[2][0]=="X":
            x=1
        elif board[0][0]=="X" and board[0][1]=="X" and board[0][2]=="X":
            x=1
        elif board[1][0]=="X" and board[1][1]=="X" and board[1][2]=="X":
            x=1
        elif board[2][0]=="X" and board[2][1]=="X" and board[2][2]=="X":
            x=1
        
        if board[0][0]=="O" and board[1][1]=="O" and board[2][2]=="O":
            o=1
        elif board[0][2]=="O" and board[1][1]=="O" and board[2][0]=="O":
            o=1
        elif board[0][2]=="O" and board[1][2]=="O" and board[2][2]=="O":
            o=1
        elif board[0][1]=="O" and board[1][1]=="O" and board[2][1]=="O":
            o=1
        elif board[0][0]=="O" and board[1][0]=="O" and board[2][0]=="O":
            o=1
        elif board[0][0]=="O" and board[0][1]=="O" and board[0][2]=="O":
            o=1
        elif board[1][0]=="O" and board[1][1]=="O" and board[1][2]=="O":
            o=1
        elif board[2][0]=="O" and board[2][1]=="O" and board[2][2]=="O":
            o=1
        
        if (x==1 and o==1) or (cx-co<0) or (cx-co>1):
            return 3
        elif cx==0 and co==0 and n==9:
            return 2
        elif x==1 and o==0 and cx>co:
            return 1
        elif x==0 and o==1 and cx==co:
            return 1
        elif x==0 and o==0 and n==0:
            return 1
        elif x==0 and o==0 and n>0:
            return 2
        else:
            return 3

    test=sys.stdin.readline()
    test=int(test)
    for z in range(test):
        board=[]
        for i in range(3):
            c=sys.stdin.readline()
            c=list(c)
            board.append(c)
        sys.stdout.write(str(ttt(board))+"\n")
except EOFError:
    pass