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

num = int(input())

try:
    if num < 10:
        raise MyError("Input is less than 10")
    elif num > 10:
        raise MyError("Input is grater than 10")
except MyError as ce:
    print("The error raised: " + ce.message)

# Assuming that we have some email addresses in the "username@companyname.com" format.
# Write program to print the user name of a given email address.
# Both user names and company names are composed of letters only.

email = str(input())
email = email.split('@')
username = email[0]
print(username)



