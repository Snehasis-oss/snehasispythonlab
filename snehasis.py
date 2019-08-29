def search1(list1,n):
    if n in list1:
        return (1)
    else:
        return (0)
n=int(input("enter the no of elements in the list\n"))
list2=[]
no=int(input("enter the no to be searched\n"))
print ("enter elements")     
for i in range(0,n):
      a=int(input())
      list2.append(a)
result=search1(list2,no)
if result==True:
      print("entered element ",(no)," is present")
else:
      print("entered element ",(no)," is not present")
            
            
