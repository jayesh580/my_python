def greaterThan(num1, num2, num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
             return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3

a = int(input("Enter first number\n"))
b = int(input("Enter second number\n"))
c = int(input("Enter third number\n"))

d = str(greaterThan(a,b, c))

print("the value of maximum number which you entered " + d)