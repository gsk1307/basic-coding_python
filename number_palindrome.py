#number is palindrome or not
a=int(input("enter the number :"))
b=str(a)
if b==b[::-1]:
    print(a,"is palindrome")
else:
    print(a,"is not a palindrome")
    
 OUTPUT:
 enter the number :45654
45654 is palindrome
