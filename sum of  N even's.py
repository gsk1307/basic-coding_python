#sum of even numbers
n=int(input("enter n :"))
c=0
for i in range(n+1): #(or) for i in range(0,n+1,2):
    if i%2==0:
        c=c+i
   
print(c,"sum of even")
