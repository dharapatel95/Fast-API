try:
    print(10/2)
    print(10/0)
    print(10/5)   #not going to execute because line 3 is throw errer and except is run
except:
    print(10/1)
finally:
    print("Hello")
