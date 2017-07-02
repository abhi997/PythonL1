#7.	Write program to convert prefix/net mask to IP
#eg: input:16  output: 255.255.0.0
num = int(input("Enter a number(less than or equal to 32)"))


nu = num % 8
def calc(num):
    if num == 7:
        return 254
    
    elif num == 6:
        return 252
    
    elif num == 5:
        return 248
    
    elif num == 4:
        return 240
    
    elif num == 3:
        return 224
    
    elif num == 2:
        return 192
    
    elif num == 1:
        return 128
    
    else:
        return 0
res = 0 
res = int(num/8)
#print(res)

if res == 4:
    print("255.255.255.255")

elif res == 3:
    print("255.255.255.{0}".format(calc(int(nu))))

elif res == 2:
    print("255.255.{0}.0".format(calc(int(nu))))

elif res == 1:
    print("255.{0}.0.0".format(calc(int(nu))))

else:
    print("{0}.0.0.0".format(calc(int(nu))))

