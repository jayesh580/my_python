grade = int(input("Enter your marks\n"))

if(grade >=90 and grade<100):
    print("Exellent! Your grade is EX")
elif(grade >=80 and grade<90):
    print("Good! Your grade is A")
elif(grade >=70 and grade<80):
    print("Best! Your grade is B")
elif(grade >=50 and grade<70):
    print("Next time do better than this! Your grade is C")
elif(grade<=50):
    print("Sorry you are failed! Your grade is F")