# age validation for the driving the car

def checkDriverAge(name, age):
    if age <= 17:
        return " Sorry {}. you are too young to drive this car. Powering off.".format(name)
    elif age == 18:
        return " Congratulations {} on your first year of driving. Enjoy the ride!".format(name)
    else:
        return " Powering On. Enjoy your ride {}!".format(name)


name = input(" What is your name = ")
age = int(input(" What is your age = "))

print(checkDriverAge(name, age))
