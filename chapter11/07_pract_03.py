class Employee:
    salary = 1000
    increment = 1.5
    @property
    def salaryAfterIncrement(self):
        return self.salary * self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, sal):
        self.increment = sal/self.salary

a = Employee()
print(a.salaryAfterIncrement)
print(a.increment)
a.salaryAfterIncrement = 2000
print(a.salaryAfterIncrement)
print(a.increment)
a.salaryAfterIncrement = 3000
print(a.salaryAfterIncrement)
print(a.increment)