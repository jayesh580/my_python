while(True):
    print("Enter q for quit this game")
    a = input("Enter the number: ")
    if a == 'q':
        break
    try:
        a = int(a) 
        if a>6:
            print("Yes! you entered greater than 6 number")
        else:
            print("You entered less than 6 number")
    except Exception as e:
        print(e)


print("Thenks for playing the game")
