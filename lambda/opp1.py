class Account:
    min_bal=500

    def open_acc(self):
        print("Ypur account is opened")
    def deposit_amount(self):
        print("Amount is deposited")
    def withdrawal(self):
        print("Widhraw ammount")
    
a1=Account()

a1.open_acc()
a1.deposit_amount()
a1.withdrawal()
print(a1.min_bal)