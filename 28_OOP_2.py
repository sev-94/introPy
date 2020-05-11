class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self.name}, and I am {self._age} years old')

player1 = PlayerCharacter('andrei', 100)
print(player1._name)
'''
player1 = PlayerCharacter('andrei', 100)
print(player1.name)
print(player1.age)

player2 = {'name': 'andrei', 'age': 100}
print(player2['name'])
print(player2['age'])
'''