def inchCoverter(n):
    conv = n * 2.54
    return conv

a = int(input("Enter the number to convert inch into cms: \n"))

b = inchCoverter(a)

print(b)