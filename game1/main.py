import random
randNumber = random.randint(1, 100)
print(randNumber)
you = None
guess = 0


while(you!=randNumber):
    you = int(input("Enter your guess : "))
    guess += 1
    if(randNumber == you):
        print("You entered write number")
    else:
        if(you < randNumber):
            print("You entered wrong number! your number is less")
        else:
            print("You entered wrong number! your number is heigher")

print(f"Your guesses is {guess}")

with open("D:\python\game1\heighscore.txt", 'r') as f:
    heighscore = int(f.read())

if(guess<heighscore):
    with open("D:\python\game1\heighscore.txt", 'w') as f:
        f.write(str(guess))
    print("Congratulations! You made an highscore")