class Pets:
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Tom(Cat):
    def sing(self, sounds):
        return f'{sounds}'

my_cats = [Cat('Simon',4),Cat('Sally',6),Cat('Tom',10)]
my_pets = Pets(my_cats)
my_pets.walk()




class Toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age
    def __str__(self):
        return f'{self.color}'
    
        
action_figure = Toy('red',0)
print(action_figure.__str__())




class SuperList(list):
    def __len__(self):
        return 1000

super_list = SuperList()
print(len(super_list))
super_list.append(3)
super_list.append(13)
super_list.append(4)
for item in super_list:
    print(item, end=' ')
print('')






