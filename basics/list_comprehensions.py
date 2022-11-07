# list
my_list = [char for char in 'hello']
my_list2 = [num for num in range(0,100)]
my_list3 = [num ** 2 for num in range(0,20)]
my_list4 = [num ** 2 for num in range(0,20) if num % 2 == 0]
print(my_list4)

#set 
my_set = {char for char in 'hello'}
my_set2 = {num for num in range(0,100)}
my_set3 = {num ** 2 for num in range(0,20)}
my_set4 = {num ** 2 for num in range(0,20) if num % 2 == 0}
print(my_set4)

# dictionary
simple_dict = {
    'a' : 1,
    'b' : 2
}

my_dict = {k:v*2 for k,v in simple_dict.items()}
print(my_dict)
my_dict2 = {num:num*2 for num in [1,2,3]}
print(my_dict2)


some_list = ['a','b','c','b','d','m','n','n']

# for item in some_list:
#     if some_list.count(item) > 1:
#         print(item,' ', end=' ')
# print('')
duplicates = list(set([item for item in some_list if some_list.count(item) > 1]))
print(duplicates)