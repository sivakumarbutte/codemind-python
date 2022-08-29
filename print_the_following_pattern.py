tmp=int(input())
n=tmp
c=[]
for i in range(n):
    c.append(n)
    n-=1
for i in range(tmp):
    for j in range(len(c)):
        print(c[j],end=' ')
    print()    