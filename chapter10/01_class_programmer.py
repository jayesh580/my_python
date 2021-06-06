class programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of the company is {self.company} Your name is {self.name} and your product is {self.product}")

jayesh = programmer("Jayesh", "python")
softy = programmer("geeta", "cutest girl in the world")

jayesh.getInfo()
softy.getInfo()
