def greater_than_5(num):
    if num>5:
        return True
    else:
        return False

l = [1, 2, 3, 4, 8, 12, 33, 44, 54, 66]
print(list(filter(greater_than_5, l)))