my_list = [1,2,3,4,5,6,7,8,9,10]
suma = 0
for item in my_list:
    suma+=item
print(suma)

for item in range(0,3):
    print('pyming')

for i,char in enumerate(list(range(100))):
    if i == 50:
        print(f'The index of 50 is {char}')

for i,char in enumerate(my_list):
    print(i,char)

picture = [
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0]
]

for item in picture:
    for pixel in item:
        if pixel == 0:
            print(' ',end='')
        else:
            print('*',end='')
    print('')

some_list = ['a','b','c','b','d','m','n','n']

for item in some_list:
    if some_list.count(item) > 1:
        print(item,' ', end=' ')
print('')