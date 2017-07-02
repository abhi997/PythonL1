str = input("enter a string")
ls = list(str)
count = 0
for i in range(len(str)):
    if(ls[i] =='e'):
        count+=1
if(count ==2):
    print("true")
else:
    print("false")
