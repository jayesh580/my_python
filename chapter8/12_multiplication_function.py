def mulFunc(no):
    for i in range(1, 11):
        print(f"{str(i)}X{str(no)}={str(i*no)}")


mul = int(input("Enter the number of multiplication\n"))

mulFunc(mul)