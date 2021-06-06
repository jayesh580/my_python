f1 = "D:\python\chapter9\jay.txt"
f2 = "D:\python\chapter9\jay1.txt"

with open(f1) as f:
    file1 = f.read()

with open(f2) as f:
    file2 = f.read()

if file1==file2:
    print("Yes! thes files are identical")
else:
    print("These files are not identical")