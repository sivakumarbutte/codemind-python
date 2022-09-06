n=int(input())
c=[]
while(n):
    r=n%10
    c.append(r)
    n//=10
print(max(c))    