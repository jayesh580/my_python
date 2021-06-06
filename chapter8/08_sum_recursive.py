# def sum_recursive(n):
#     total = sum_recursive(n-1) + n
#     return total
        
# i = int(input("Enter the number for sum of recursive: "))
# f = sum_recursive(i)
# print(f)

# Python program to find the sum of natural using recursive function

def recur_sum(n):
#    if n <= 1:
#        return n
#    else:
    return n + recur_sum(n-1)

# change this value for a different result
num = 3

if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",recur_sum(num))