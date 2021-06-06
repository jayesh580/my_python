class getRich:
    def __init__(self, n, j):
        self.name = n 
        self.money = j

    def user(self):
        pass

    def storeMoney(self):
        with open("D:\python\Project\store.txt", 'r') as f:
            read = f.read()

        with open("D:\python\Project\store.txt", 'w') as f:
            write = f"{self.money + int(read)}"
            f.write(str(write))

user1 = getRich("jayesh", 25)
user1.storeMoney()
user2 = getRich("amol", 25)
user2.storeMoney()