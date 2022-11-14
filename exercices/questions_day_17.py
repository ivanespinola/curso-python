# Please write assert statements to verify that every number in the list [2,4,6,8] is even.

my_list = [2,4,6,8]

for element in my_list:
    assert element % 2 == 0, f'{element} is not a even number'

# Please write a program which accepts basic mathematic expression from console and print the evaluation result.

expression = input()
result = eval(expression)
print(result)
    

# Please write a binary search function which searches an item in a sorted list.
# The function should return the index of element to be searched in the list.

def search_function(list, index):
    lower = 0
    upper = len(list)
    print('Array Length:',upper)
    while lower < upper:
        mid = (lower + upper) // 2
        print('Middle Value:',mid)
        value = list[mid]
        if index == value:
            return mid
        elif index > value:
            lower = mid
        elif index < value:
            upper = mid

# Please generate a random float where the value is between 10 and 100 using Python module.

import random 

def random_float():
    random_number = random.uniform(10,100)
    print(random_number)

random_float()

