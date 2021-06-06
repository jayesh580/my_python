content = True
i = 1
with open("D:\python\chapter9\log.txt","r") as f:
    while content:
        content = f.readline()
        if "python" in content.lower():
            print(content)
            print(f"Your search reasult present in line number {i}")
        i+=1