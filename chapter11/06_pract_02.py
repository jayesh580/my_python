class animal:
    pass 

class pets(animal):
    pass 

class dogs(pets):
    @staticmethod
    def bark():
        print("bow bow")

d = dogs()
d.bark()