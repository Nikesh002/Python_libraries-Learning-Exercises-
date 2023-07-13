#  Print names using function
def name(name):
    print("Hi ", name)


n = name("Jim")
n = name("Sam")


#  Print names using class & object
class name:
    name = ""

    def __init__(self, name):
        self.name = name
        print("Hi ", self.name)


n = name("Jim")
n = name("Sam")
