#prime number or not
num=int(input("enter the number :"))
c=0
for i in range(1,num+1):
    if num%i==0:
        c=c+1
    if c==3: #if num has more than 2 divisibles then it is not a prime
        break
if c==2:
    print(num,"is prime")
else:
    print(num,"is not a prime")
        
