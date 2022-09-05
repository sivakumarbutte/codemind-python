a=int(input())
b=int(input())
sum=0
for i in range(1,a):
    if(a%i==0):
        sum=sum+i
tmp=0
for j in range(1,b):
    if(b%j==0):
        tmp=tmp+j
if(sum==b and tmp==a):
    print('Amicable')
else:
    print('Not Amicable')