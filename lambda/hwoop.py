class Account:
    branch_name="SBI"
    min_bal=600

    def __init__(self,id,name,amount):
        self.name=name
        self.id=id
        self.bal=amount
    def open_acc(self):
        print("Account successfully opened")
    def deposite_amount(self,amount):
        self.bal=self.bal+amount
    def widhrowal_amount(self,amount):
        self.bal=self.bal-amount 
    def get_bal(self):
        return self.bal-self.min_bal
       
a1=Account(101,"Parth",5000)
a2=Account(102,"Savan",6000)
a3=Account(103,"Shreya",4000)
print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)

a1.open_acc()
a1.deposite_amount(3000)
a1.get_bal()

print("---------------------------------------------------")
#print(Account.__dict__)
print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)
