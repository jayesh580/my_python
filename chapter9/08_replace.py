with open('D:\python\chapter9\sample.txt', 'r') as f:
    a = f.read()
a=a.replace("terrorist", "#####")

with open('D:\python\chapter9\sample.txt', 'w') as f:
    f.write(a)