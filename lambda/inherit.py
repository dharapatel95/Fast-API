class Parent:
    def m1(self):
        print("m1 method of parent class")
    def m2(self):
        print("m2 method of parent class")

class Child(Parent):
    def m3(self):
        print("m3 method of parent class")
    def m4(self):
        print("m4 method of parent class")

p1=Parent()
c1=Child()
p1.m1()
p1.m2()
c1.m1()
c1.m2()
c1.m3()