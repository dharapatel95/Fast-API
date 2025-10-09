class InsuffientBalErr(Exception):
    def __init__(self, msg):
        self.msg=msg

def widhrow(amount):
    acc_bal=500
    if amount<acc_bal:
        print("Widhrow successfully!!!")
    else:
        try:
            raise InsuffientBalErr("Your balance is low!")
        except InsuffientBalErr as err:
            print(err)


amount=int(input("How much money you want to widhrow?  "))
widhrow(amount)