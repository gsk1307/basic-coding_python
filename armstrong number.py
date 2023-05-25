n=int(input("enter the num :"))
a=str(n)
b=len(a)
c=0
for i in range(b):
    d=(int(a[i]))**b
    c=c+d
if c==n:
    print(n,"is armstrong number")
else:
    print(n,"is not a armstrong")
    
    
