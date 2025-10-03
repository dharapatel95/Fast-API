def outer():
    print("Outer function started")

    def inner():
         print("inner function")
    inner()  


outer()
