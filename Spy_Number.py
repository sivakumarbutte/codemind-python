n=int(input())
sum=0
product=1
while(n):
    d=n%10
    sum=sum+d
    product=product*d
    n//=10
if(sum==product):
    print('Spy Number')
else:
    print('Not Spy Number')