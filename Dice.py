import random

while True:
    throw_dice = input(" Press yes/no to throw the Dice.. ").lower()
    if throw_dice != "yes":
        if throw_dice == "no":
            print(" Good Bye ! ")
            break
        print(" Please enter a valid input next time.. ")
        continue
    else:
        dice = random.randrange(0, 7)
        print(" Number is = ", dice)


