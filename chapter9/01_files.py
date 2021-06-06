i = 2
f = open(f"D:\python\chapter9\tables/sample{i}.txt",'w')
# data = f.read(5) # read only first 5 character from the file
data = f.write('hii')
f.close()
