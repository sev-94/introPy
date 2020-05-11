class PlayerCharacter:
    membership = True  # Class Object Attribute

    def __init__(self, name='anonymous', age=0):  # Constructor Function
        #if (self.membership):
            #if (age > 18):
        self.name = name
        self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    @classmethod
    def adding_things(cls, num1, num2):
            return cls('Teddy', num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


#player1 = PlayerCharacter('Cindy', 10)
player2 = PlayerCharacter('Tom', 21)
player2.attack = 50

#print(player1)
print(player2)
print(player2.attack)

print(PlayerCharacter.adding_things(2,3))

player3 = PlayerCharacter.adding_things(2,3)
print(player3.adding_things(2,3))
