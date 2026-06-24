def even(a,b):
    for i in range(a,b+1,2):
        if(i%2==0):
           print(i)
        else:
            break
a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
print(even(a,b))