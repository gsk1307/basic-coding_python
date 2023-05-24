#sorting
n=int(input("enter number of values :"))
list1=[]
for i in range(n):
    a=int(input("enter the value :"))
    list1.append(a)
print(list1, "before sorting")
list1.sort()
print(list1, "after sorting")
