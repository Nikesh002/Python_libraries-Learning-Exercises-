# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
c1 = Cat("Lili", 1)
c2 = Cat("Lucy", 5)
c3 = Cat("July", 3)


# 2 Create a function that finds the oldest cat
def oldest_cat():
    if c1.age > (c2.age and c3.age):
        return c1.name + " & it is " + str(c1.age)
    elif c2.age > (c1.age and c3.age):
        return c2.name + " & it is " + str(c2.age)
    else:
        return c3.name + " & it is " + str(c3.age)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print("The oldest cat is {} years old.".format(oldest_cat()))
