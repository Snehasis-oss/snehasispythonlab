n=int(input("Enter the no of fibonacci nos to generate \n"))
a=o
b=1
print(a)
print(b)
for i in range(2,n):
    c=a+b
    print(c)
    a=b
    b=c
            
