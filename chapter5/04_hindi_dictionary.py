dictionary = {
    "aadmi" : "man",
    "haathi":"eliphant",
    "sher":"tiger",
    "sanganak":"computer",
    "baccha":"kid"
}
print("Your options are", dictionary.keys())
a = input("Enter the Hindi word:\n")
#print("Meaning of your word is", dictionary[a])
print("Meaning of your word is", dictionary.get(a))