# # mul = int(input("Enter the number of multiplication\n"))
# for i in range(1, 11):
#     # print(f"{str(i)}X{str(mul)}={str(i*mul)}")
#     print(f"{i}")


for i in range(9,0,-1): #From 9 to 1, decrement by 1 each time. range (the starting number, the last number (but not including this number), the number of increments each time (decrement is a negative number))
	 for j in range(i,0,-1): #Start from i and decrease by 1 each time
		 print(str(i)+"*"+str(j)+"="+str(i*j),end=" ") #Output formula, the usage of this end is the first time I see it, which means to follow Is not a newline, but a space
	 print() #New line after outputting a line, no need to add "\n" in parentheses