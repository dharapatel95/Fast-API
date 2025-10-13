class Account:
    def __init__(self,id,name,amount):
        self.id=id
        self.name=name
        self.amount=amount
    def open_acc(self):
        print("Account successfully opened.")
    def deposite_ammount(self,amount):
        print(amount,"- Amount deposited")

a1=Account(101,"Dhara",2000)
print(a1.open_acc())
print(a1.deposite_ammount(1000))
print(a1.__dict__)