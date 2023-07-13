# OOP

# Class - Blueprint for the creating the objects
# Objects - instance, created as many times as you want
# Attributes - Characteristics associated to a type(obj.)
# Methods - Functions associated to a type

class ConstDest:
    x = 0

    def __init__(self, color, type):
        self.color = color
        self.type = type
        print("Constructed")

    def __del__(self):
        print("Destructed")


cd = ConstDest("Red", "Mini")
print(cd.color)
print(cd.type)
cd.__del__()
print(cd.type)
