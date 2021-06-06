class vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[1]}k"      

c1 = vector([1,2,3])
c2 = vector([6,5,4])
print(c1)
print(c2)