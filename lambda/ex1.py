product_price=[98,198,298,398]

def addplus(price):
    return price+1

a=map(addplus,product_price)
b=list(a)
print(b)