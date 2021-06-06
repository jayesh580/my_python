class calculator:
    def __init__(self, num):
        self.number = num

    def squarNum(self):
        square = self.number * self.number
        print(f"The sqare of number {self.number} is {square}")

    def cubeNum(self):
        cube = self.number * self.number * self.number
        print(f"The cube of number {self.number} is {cube}")

    def squareRootNum(self):
        squareroot = self.number **0.5
        print(f"The squareroot of number {self.number} is {squareroot}")

    @staticmethod
    def greet():
        print("*********Welcome to this easy calculator*********")


a = calculator(3)
a.greet()
a.squarNum()
a.cubeNum()
a.squareRootNum()