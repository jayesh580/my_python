def divisible_by_5(num):
    if num%5 == 0:
        return True
    else:
        return False

# b = lambda a: a%5 == 0
list1 = [5, 15, 7, 2, 4, 50]
print(list(filter(divisible_by_5,list1)))
# print(list(filter(b,list1)))
