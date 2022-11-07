
from functools import reduce
from hashlib import new
import math


my_list = [1,2,3]
# def multiply_by2(item):
#     return item * 2

print(list(map(lambda item: item * 2, my_list)))

# def only_odd(item):
#     return item % 2 != 0

print(list(filter(lambda item: item % 2 != 0, my_list)))


# def combine_numbers(acc , item):
#     return acc + item

print(reduce(lambda acc, item: acc + item, my_list))

# Square
my_list2 = [5,4,3]
print(list(map(lambda item: math.floor(math.pow(item,2)), my_list2)))

# List sorting
a = [(0,2), (4,3), (9,9), (10,-1)]
a.sort(key = lambda x: x[1])
print(a)

