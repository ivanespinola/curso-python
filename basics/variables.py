from datetime import datetime

print('What year where you born? ')
birth_year = int(input())
actual_year = datetime.now().year
age = actual_year - birth_year
print(f'Your age is {age}')

username = input('Username: ')
password = input('Password: ')
longitud = len(password)
secret_password = '*' * longitud
print(f'{username}, your password {secret_password} is {longitud} letters long')



