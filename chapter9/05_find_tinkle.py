with open('D:\python\chapter9\poems.txt', 'r') as f:
    a = f.read()
# f = open("D:\python\chapter9\poems.txt",'r')
# print(a.get('twinkle'))
if 'twinkle' in a:
    print("Twinkle is present")
else:
    print("Twinkle is not present")
