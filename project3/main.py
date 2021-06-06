import random
class Server:
    def __init__(self, list):
        self.list = list
        self.path = "D:\python\project3/user.txt"
        
    def checkUser(self):
        dic = self.list
        while(True):
            msg1 = "\n Please Enter username and password correctly"
            print(msg1)
            a = input("Enter your username = ")
            b = input("Enter Your Password = ")
            if a in dic:
                if dic[a] == b:
                    print("Username or password is correct")
                    break
                else:
                    print("username or password is incorrect! Try again")
            else:
                print("username or password is incorrect! Try again")

    def registerUser(self):
        d = {}
        with open("D:\python\project3/user.txt", 'r') as f :
            for line in f:
                (key, val) = line.strip().split(', ')
                d[key] = val
        dic = d

        d1 = {}
        with open("D:\python\project3/referal.txt", 'r') as f :
            for line in f:
                (key, val) = line.strip().split(', ')
                d[key] = val
        dic1 = d1

        ref = random.randint(500, 700)

        c = 25
        msg2 = "\nEnter your details"
        a = input("Enter username :")
        b = input("Enter password :")

        while(True):
            if a in dic :
                print("this username is already in use please type another username")
                break
            else:
                with open("D:\python\project3/user.txt", 'a') as f:
                    f.write(f"\n{a}, {b}")
                with open("D:\python\project3/bank.txt", 'a') as f:
                    f.write(f"\n{a}, {c}")
                with open("D:\python\project3/referal.txt", 'a') as f:
                    f.write(f"\n{a}, {ref}")
                print("Thanks for register in safe market! Please login and enjoy our services")
                break
if __name__ == "__main__":

    d = {}
    with open("D:\python\project3/user.txt", 'r') as f :
         for line in f:
             (key, val) = line.strip().split(', ')
             d[key] = val
    dictionary = Server(d)

    while(True):
        welcomeMsg = '''\n ======Hey there welcome to Safe Marker======
        Where you can invest less amount of money and get heigher profit on it
        1. Login
        2. Register
        3. Admin Login
        4. Forgot Password
        5. exit
        '''
        print(welcomeMsg)
        a1 = int(input("Enter Your Choice : "))
        if a1 == 1:
            dictionary.checkUser()
        elif a1 == 2:
            dictionary.registerUser()
        elif a1 == 3:
            pass
        elif a1 == 4:
            pass
        elif a1 == 5:
            print("Thanks for visiting! Have a good day :) ")
            exit()