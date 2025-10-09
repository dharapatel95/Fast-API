a=None
b=None

try:
    a=int(input("Enter 1st number:"))
    b=int(input("Enter 2nd number:"))
    print(a/b)
except ZeroDivisionError as err:
    print(err)
    
print("hello")