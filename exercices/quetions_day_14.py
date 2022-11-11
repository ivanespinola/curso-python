# Write a function to compute 5/0 and use try/except to catch the exceptions.

def exceptions():
    num1 = int(input('Enter one number: '))
    num2 = int(input('Enter another number: '))
    try:
        print(num1 / num2)
    except ZeroDivisionError:
        print('Please enter a number higher than 0')
    finally:
        print('Done!')

exceptions()

# Define a custom exception class which takes a string message as attribute.

class MyError(Exception):
    def __init__(self, message):
        self.message = message


