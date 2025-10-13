class Demo:
    a=100

    def m1(self):
        self.b=200
    @classmethod
    def m2(cls):
        cls.c=300
        Demo.d=400
    def m3():
        Demo.e=500
a=Demo()
a.f=600
a.m1()
a.m2()


a1=Demo()
print(a.__dict__)
print(a1.__dict__)
print(Demo.__dict__)

