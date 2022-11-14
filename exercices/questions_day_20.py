# Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].

my_list = [5,6,77,45,22,12,24]
new_list = [x for x in my_list if x % 2 != 0]
print(new_list)

# By using list comprehension, please write a program to print the list after removing numbers
#  which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

my_list2 = [12,24,35,70,88,120,155]
new_list2 = [x for x in my_list2 if x % 5 != 0 and x % 7 != 0]
print(new_list2)

# By using list comprehension, please write a program to print the list
# after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

my_list3 = [12,24,35,70,88,120,155]
new_list3 = [x for index, x in enumerate(my_list3) if index not in [0, 2, 4, 6]]
print(new_list3)

# By using list comprehension, please write a program to print the list 
# after removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].

my_list4 = [12,24,35,70,88,120,155]
new_list4 = [x for index, x in enumerate(my_list4) if index not in [2, 4]]
print(new_list4)

# By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0

array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
print(array)