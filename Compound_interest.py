p,r,t=map(int,input().split())
A = p*(1 + r/100)**t
res="{:.2f}".format(A)
print(res)