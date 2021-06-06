letter='''Dear name 
You are selected!
date '''
a = input("Enter your name: ")
b = input("Enter date: ")
letter = letter.replace("name", a)
letter = letter.replace("date", b)
print(letter)