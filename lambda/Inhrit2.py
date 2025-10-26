class parent1():
    def m1(self):
        print("Parent1 - m1 method")
    def m2(self):
        print("parent1 - m2 method")
class parent2():
    def m3(self):
           print("parent2 - m3 method")
    def m4(self):
           print("parent2 - m4 method")
class child(parent1,parent2):
     def m5(self):
          print("child - m5 method")

c1=child()
c1.m1()
c1.m2()
c1.m3()
c1.m4()
c1.m5()