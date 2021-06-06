def game():
    return 41

score = game()

with open('D:\python\chapter9\heightscore.txt', 'r') as f:
    heightscore = f.read()
   
if heightscore == '':
    with open('D:\python\chapter9\heightscore.txt', 'w') as f:
        f.write(str(score)) 

elif int(heightscore) < score:
    with open('D:\python\chapter9\heightscore.txt', 'w') as f:
        f.write(str(score))

with open('D:\python\chapter9\heightscore.txt', 'r') as f:
    heightscore = int(f.read())
print(heightscore)