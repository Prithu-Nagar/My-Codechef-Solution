try:
    t=int(input())
    while t>0:
        s=input()
        counter=0
        if s[0]=='1':
            counter+=1
        for i in range(1,len(s)):
            if s[i]=='1' and s[i-1]!=s[i]:
                counter+=1
        print(counter)
        t-=1
except EOFError:
    pass