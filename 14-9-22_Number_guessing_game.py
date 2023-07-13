import random
import sys

try:
    start_num = int(sys.argv[1])
    end_num = int(sys.argv[2])
except ValueError:
    print(" Please enter the valid integers as the parameters ")
else:
    random_num = random.randint(start_num, end_num)
    print(" Welcome to Number Guessing Game !!!")
    while True:
        try:
            guessed_num = int(input(f" Guess the number between {start_num} & {end_num} = "))
            if guessed_num in range(start_num, end_num):
                if guessed_num == random_num:
                    print(" You guess is correct !!!")
                    break
                else:
                    print(" Sorry your guess in not correct. please try again")
            else:
                print(" Please enter the number from the given range. ")

        except ValueError:
            print(" Please enter the valid number ")
