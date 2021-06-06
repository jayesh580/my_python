def tempConverter(cel):
    temp = (cel * 9/5) + 32
    return temp 

a = int(input("Enter the temperature in celcious:\n"))

b = str(tempConverter(a))

print("Your Entered temperature in faranhide is " + b)