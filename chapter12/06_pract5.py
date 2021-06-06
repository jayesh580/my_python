num = int(input("Enter the number for multiplication : "))

list = [num*i for i in range(1, 11) ]

print(list)

with open("D:\python\chapter12/table.txt", 'a') as f :
    f.write(str(list))
    f.write("\n")