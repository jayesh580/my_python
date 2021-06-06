sub1 = int(input("Enter marks of 1st subject : "))
sub2 = int(input("Enter marks of 2nd subject : "))
sub3 = int(input("Enter marks of 3rd subject : "))

if (sub1<35 or sub2<35 or sub3<35):
    print("You are fail because you have less than 35 in one of above subject")

elif (sub1+sub2+sub3/3 < 40):
    print("You are fail because you have less than 40 in subject")

else : 
    print("Congratulations! You are passed")