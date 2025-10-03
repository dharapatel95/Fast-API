def outer():
    print("Outer function")

    def inner():
        print("inner function")

    return inner

inn=outer()
print(type(inn))
inn()  #by this way we can print inner function outside of outer #function
inn()