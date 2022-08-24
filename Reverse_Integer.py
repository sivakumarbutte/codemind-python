a=int(input())
if(a>=0):
    rev=str(a)[::-1]
    rev=int(rev)
    print(rev)
else:
    a=abs(a)
    rev=str(a)[::-1]
    rev=int(rev)
    res="-"+str(rev)
    print(res)
    