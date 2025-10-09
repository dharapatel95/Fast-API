try:
    fp=open('abc.txt','r')
    data=fp.read()
    print(data)
except:
    fp=open('appl.txt','r')
    data=fp.read()
    print(data)
finally:
    print("This block of code is always execut")