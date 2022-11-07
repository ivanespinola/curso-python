class PlayerCharacter:
    #class obj attribute
    membership = True 
    def __init__(self, name,age):
        self.name = name #attributes
        self.age = age
    def run(self):
        return f'{self.name}, {self.age}'

print(PlayerCharacter.membership)
player1 = PlayerCharacter('Ivan',23)
print(player1.run())

cat_ages = []
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def oldest_cat(*args):
        return max(args)       
    

cat1 = Cat('Tom',1)
cat2 = Cat('Ali',6)
cat3 = Cat('Hugo',4)
print(f'The oldest cat is {Cat.oldest_cat(cat1.age,cat2.age,cat3.age)} years old ')


class User:
    def __init__(self, email):
        self.email = email
    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power
    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
    def attack(self):
        print(f'attacking with arrows: arrows left- {self.num_arrows}')
    
        
wizard = Wizard('Merlin',60,'merlin@gmail.com')
archer = Archer('Robin',160)
wizard.attack()
archer.attack()
print(wizard.email)
