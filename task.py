import json,csv
#responce=requests.get('https://jsonplaceholder.typicode.com/users')
fp=open('users.json','r')
users=json.load(fp)
print(type(fp))
employees=[]
for user in users:
    employees.append([user['id'],user['username']])

fp1=open('user.json','w')
json.dump(users,fp1)
print("New user.json file is created.")

fp2=open('user.csv','w')
cw=csv.writer(fp2)
cw1=cw.writerows(employees)
print("New user.csv file is created.")
print(employees)


fp.close()
fp1.close()
fp2.close()