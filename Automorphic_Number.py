a=int(input())
b=a*a
c=len(str(a))
res=b%(10**c)
if(res==a):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")