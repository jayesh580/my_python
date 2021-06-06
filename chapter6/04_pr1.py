a = int(input("Enter number1 : \n"))
b = int(input("Enter number2 : \n"))
c = int(input("Enter number3 : \n"))
d = int(input("Enter number4 : \n"))

# if(a>b and a>c and a>d) : 
#     print("Greatest number is ", a)
# if(b>a and b>c and b>d) : 
#     print("Greatest number is ", b)
# if(c>a and c>b and c>d) : 
#     print("Greatest number is ", c)
# if(d>a and d>b and d>c) : 
#     print("Greatest number is ", d)

# also

if(a>d):
    f1 = a
else :
    f1 = d 

if(b>c):
    f2 = b
else :
    f2 = c

if(f1>f2) :
    print(str(f1) + " Is greatest number")
else : 
    print(str(f2) + " Is greatest number")