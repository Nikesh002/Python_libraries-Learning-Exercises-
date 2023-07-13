import random

print(" This is the Number Guess game!!!")
name = input(" Please enter your name: ")


while True:

    print("\n Hey "+name+", we are about to start the game & you have 6 chances to guess the number between 1 to 20.\nSo,Good luck!!!\n")

    secretNum = random.randrange(1, 20)

    for guessNum in range(1, 7):
        num = int(input(" Enter your guess : "))
        if num > secretNum:
            print(" Your guess is too high.")
        elif num < secretNum:
            print(" Your guess is too low.")
        else:
            break

    if num == secretNum:
        print("You have guessed the correct number in "+str(guessNum)+" chances.")
    else:
        print("You are failed. The correct number was "+str(secretNum))
    rePlay = input(" Do you want to play again? (yes/no) :")
    if rePlay.lower() == "no":
        print(" Thanks for playing this game...")
        break
    elif rePlay.lower() == "yes":
        print(" Let's play again")
    else:
        print(" You have entered invalid option. ")
        break
