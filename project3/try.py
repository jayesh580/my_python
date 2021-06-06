class anything:
    def __init__(self, list):
        self.list = list   
 
    def showBalance(self, name):
        print(f"\nYour Balance is : {self.list[name]}")   

    def withdrawMoney(self):
        pass
        # with open("", 'w') as f:
        #     f.write()

l = {}
with open("D:\python\project3/bank.txt", 'r') as f:
    for line in f:
        (key, val) = line.strip().split(', ')
        l[key] = val


dictionary = anything(l)


while(True):
    username = "Jayesh580"
    referal = "112233"
    print(f"\n=====Welcome {username} Your referal code is {referal}=====")
    p = '''\nChose your option
    1. Show my balance
    2. Withdraw Money
    3. Your price
    4. Back to the login page
    '''
    print(p)
    a = int(input("Enter Your Choice Here : "))
    if a == 1:
        dictionary.showBalance(username)
    elif a == 2:
        pass
    elif a == 3:
        pass
    elif a == 4:
        print("Thanks for visiting")
        exit()