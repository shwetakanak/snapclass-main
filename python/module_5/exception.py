try:
    x=int(input("Enter x"))
    ans=10/x

except ZeroDivisionError:
    print("Division by zero is not allowed")

else:
    print(ans)