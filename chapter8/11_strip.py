def changeString(string, word, name):
    newStr = string.replace(word, name)
    return newStr.strip()




this = "     jayesh is a good boy      "
e = input("Enter the name to replace:\n")
n = changeString(this, "jayesh", e)

print(n)
# print(this)
# print(this.strip())