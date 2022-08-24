a=int(input())
for i in range(a):
    if(a==i*(i+1)):
        print("YES")
        break
else:
    print("NO")