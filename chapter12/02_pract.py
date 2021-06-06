def readFile(filename):
    try:
        with open(f"D:\python\chapter12\{filename}", 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"{filename} file is not found")
        # print(FileNotFoundError)

    # except Exception as e:
    #     print(f"{filename} file is missing")
readFile("file1.txt")
readFile("file2.txt")
readFile("file3.txt")