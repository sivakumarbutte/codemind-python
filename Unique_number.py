n=int(input())
l=len(str(n))
c=[]
while(n!=0):
    t=n%10
    c.append(t)
    n//=10
a=set(c)
b=list(a)
m=len(b)
if(l==m):
    print('Unique Number')
else:
    print('Not Unique Number')