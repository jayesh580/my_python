filename = "D:\python\project3/user.txt"
d = {}
with open(filename, 'r') as f :
    for line in f:
        (key, val) = line.strip().split(', ')
        d[key] = val
print(d)