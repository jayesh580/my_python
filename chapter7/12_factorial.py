num = int(input("Enter the number for factorial: "))
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i

print(f"Factorial of {num} is {factorial}")