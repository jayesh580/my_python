# (a+bi)(c+di) = (ac−bd) + (ad+bc)i
class complex:
    def __init__(self, r, i):
        self.real = r
        self.imaginory = i

    def __add__(self, c):
        return complex(self.real + c.real, self.imaginory + c.imaginory)

    def __mul__(self, c):
        mulReal =  self.real*c.real - self.imaginory*c.imaginory
        mulImg =  self.real*c.imaginory + self.imaginory*c.real
        return complex(mulReal, mulImg)

    def __str__(self):
        if self.imaginory<0:
            return f"{self.real} - {-self.imaginory}i"
        else:
            return f"{self.real} + {self.imaginory}i"

c1 = complex(1, 3)
c2 = complex(2, 3)
c3 = complex(4, 5)
print(c1 + c2)
print(c1 * c2)
