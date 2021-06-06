words = ["terrorist", "donky", "kutta", "bitch", "sex"]

with open("D:\python\chapter9\gandi_list.txt","r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#####")
    with open("D:\python\chapter9\gandi_list.txt","w") as f:
        f.write(content)
        
