# This is the first OOP for test

class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return self.name, self.age


p1 = Player("Jack", 20)
p2 = Player("Jim", 30)

print(p1.display())
print(p2.display())
