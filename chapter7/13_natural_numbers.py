# Write a program to find the sum of first n natural numbers using a while loop.
i = int(input("Enter the number for find sum of natural numbers: "))
num = i
sum = 0
while(num > 0):
    sum += num
    num -= 1
print(f"sum of natural number of {i} is {sum}")
