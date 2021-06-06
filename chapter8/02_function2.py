def greet(name):
    print("Welcome " +name)
def mySum(s1, s2):
    add = s1 + s2
    return add
name = input("Enter your name ")

s1 = int(input("Enter first number"))
s2 = int(input("Enter second number"))

addition = mySum(s1, s2)
print(addition)
greet(name)

