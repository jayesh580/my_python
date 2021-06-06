#with pure data content in the list
# with open("D:\python\project2\data.txt", 'r') as f:
#     a = f.readlines()
#     li = [x.strip() for x in a]
# print(li)

#with all specific lines and gaps in the list
# with open("D:\python\project2\data.txt", 'r') as f:
#     a = [line.rstrip() for line in f]
# print(a)

# with open("D:\python\project2\data.txt", 'r') as f:
#     lines = []
#     for line in f:
#         lines.append(line.strip('\n'))
# print(lines)

# with open("D:\python\project2\data.txt", 'r') as infile:
#     data = infile.read()
# li = data.splitlines()
# print(li)

# from pathlib import Path
# p = Path('D:\python\project2\data.txt')
# lines = p.read_text().splitlines()
# print(lines)

# print([line.strip() for line in open('D:\python\project2\data.txt')])