with open("D:\python\chapter9\log.txt","r") as f:
    log = f.read()

if "python" in log.lower():
    print("Python is present in the log")
else:
    print("Python is not present in the log")