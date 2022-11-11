# Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

def print_dict():
    my_dict = {}
    for number in range(1,21):
        my_dict[number] = number**2
    print(my_dict)

print_dict()

# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
# The function should just print the keys only.

def print_dict2():
    my_dict = {}
    for number in range(1,21):
        my_dict[number] = number ** 2
    for key in my_dict:
        print(key, end=' ')
    print()

print_dict2()

# Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

def print_list():
    my_list = []
    for number in range(1,21):
        my_list.append(number**2)
    print(my_list)

print_list()

# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
# Then the function needs to print the first 5 elements in the list.

def print_list2():
    my_list = []
    for number in range(1,21):
        my_list.append(number**2)
    for element in range(0,5):
        print(my_list[element], end=' ')
    print()

print_list2()

# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
# Then the function needs to print the last 5 elements in the list.

def print_list3():
    my_list = []
    for number in range(1,21):
        my_list.append(number**2)
    for element in range(-5,0):
        print(my_list[element], end=' ')
    print()

print_list3()

# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
# Then the function needs to print all values except the first 5 elements in the list.

def print_list4():
    my_list = []
    for number in range(1,21):
        my_list.append(number**2)
    for element in range(5,20):
        print(my_list[element], end=' ')
    print()

print_list4()

# Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).

def print_tuple():
    my_tuple = ()
    tuple_to_list = list(my_tuple)
    for number in range(1,21):
        tuple_to_list.append(number**2)
    print(tuple(tuple_to_list))

print_tuple()
