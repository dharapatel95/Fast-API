#how use lambda

prices=[98,198,298,398]
p=list(map(lambda price:price+1,prices))
print(p)
print(prices)  


ename=['Dhara','Parth','Savan','Shreya','Maitry']

r=list(map(lambda enames:enames.upper(),ename))
print(r)