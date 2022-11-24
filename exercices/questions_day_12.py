# Write a program which can map() to make a list whose elements 
# are square of numbers between 1 and 20 (both included).

a = range(1,21)
square_numbers = list(map(lambda e: e**2, a))
print(square_numbers)

# Define a class named American which has a static method called printNationality.

class American:
    def __init__(self, nationality):
        self.nationality = nationality
    
    @staticmethod
    def printNationality():
        print('EEUU')

class NewYorker(American):
    def __init__(self, nationality):
        super().__init__(nationality)

person1 = American('EEUU')
person2 = NewYorker('EEUU')
print(person1)
print(person2)

