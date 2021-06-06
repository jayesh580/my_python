class train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"The name of the train you select is {self.name}")
        print(f"The numner of seats available in this train is {self.seats}")

    def fareInfo(self):
        print(f"Price of this train ticket is {self.fare}.Rs")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry seats are not available please go and book your ticket in tatkal seva center")

    def cancelTicket(self):
        pass


localtrain = train("CSMT Express: 001", 40, 200)
localtrain.getStatus()
localtrain.bookTicket()
localtrain.bookTicket()
localtrain.bookTicket()
localtrain.fareInfo()