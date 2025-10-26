class GP():
    def g1(self):
        print("Grand parent class - g1 mathod")

class Parent(GP):
    def p1(self):
        print("parent class - p1 method")
    def p2(self):
        print("parent class - p2 method")

class child(Parent):
    def c1(self):
        print("child class - c1 method")



ca=child()
ca.p1()
ca.p2()
ca.c1()
ca.g1()