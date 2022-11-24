# Write a program which accepts a sequence of comma-separated numbers 
# from console and generate a list and a tuple which contains every number.

numbers = input("Enter a sequence of numbers separated by ',' : ")
n = numbers.split(",")
print(list(n))
print(tuple(n))

# Write a program that accepts a comma separated sequence of words 
# as input and prints the words in a comma-separated sequence after sorting them alphabetically.

my_list = input("Enter words separated by ',': ").split(',')
my_list.sort()
print(my_list)

# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class Simple:
    def __init__(self):
        pass
    def getString(self):
        self.string = str(input("Enter a string: "))
    def printString(self):
        print(self.string.upper())

simple = Simple()
simple.getString()
simple.printString()