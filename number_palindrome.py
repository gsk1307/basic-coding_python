#number is palindrome or not
a=int(input("enter the number :"))
b=str(a)
if b==b[::-1]:
    print(a,"is palindrome")
else:
    print(a,"is not a palindrome")
