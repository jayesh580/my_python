friends = ["Apple", "Akash", "Rohan", 7]

text = input("Enter the text you want to search\n")

if(text in friends):
    print("This text is present in the list")
else:
    print("This text is not present in the list")