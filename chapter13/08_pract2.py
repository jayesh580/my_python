name = input("Enter Your name : ")
marks = input("Enter Your marks : ")
phone = input("Enter Your phone number : ")

# a = "The name of the student is {}, his marks are {} and the phone number is {}".format(name, marks, phone)
a = "The name of the student is {1}, his marks are {2} and the phone number is {0}".format(name, phone, marks)
print(a)