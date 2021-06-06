import os
file1 = "D:\python\chapter9\jay1.txt"
file2 = "D:\python\chapter9/renamed_file_jay1.txt"

with open(file1) as f:
    content = f.read()

with open(file2, 'w') as f:
    f.write(content)

os.remove(file1)