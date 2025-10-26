class Parent:
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
