class User(object):
    def __init__(self, email):
        self.email = email

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
        print(f'attacking with arrows: arrows left-{self.num_arrows}')

wizard1 = Wizard('Merlin', 60, 'merlin@gmail.com')
archer1 = Archer('Robin', 30)

# isinstance() is a built in function to check ig sn object is an instance of a class
print(isinstance(wizard1, User))

print(wizard1.email)

# Polymorphism - Ability to redefine/modify methods in classes
def player_attack(char):
    char.attack()

player_attack(wizard1)
player_attack(archer1)

for char in [wizard1, archer1]:
    char.attack()

#Prints a list of all the available methods for the class
print(dir(wizard1))