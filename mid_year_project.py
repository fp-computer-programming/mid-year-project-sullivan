# Author: CRS 02/10/22
# Define the chutes and ladders function
def chutes_and_ladders():
# Assign level, dice roll, and attempts variable
    attempts = 0
    level = 1
    dice_roll = int(input("Pick a number between 1 and 10."))
# Dice roll code
    if dice_roll == 1:
        level += 1
        attempts += 1
        print("You are currently on level {0}".format(level))
        dice_roll = int(input("Pick a number between 1 and 10."))
    if dice_roll == 2:
        level += 1
        attempts += 1
        print("You are currently on level {0}".format(level))
        dice_roll = int(input("Pick a number between 1 and 10."))
    if dice_roll == 3:
        level -= 1
        attempts += 1
        print("You are currently on level {0}".format(level))
        dice_roll = int(input("Pick a number between 1 and 10."))
    if dice_roll == 4:
        level += 1
        attempts += 1
        print("You are currently on level {0}".format(level))
        dice_roll = int(input("Pick a number between 1 and 10."))
    if dice_roll == 5:
        level -= 1
        attempts += 1
        print("You are currently on level {0}".format(level))
        dice_roll = int(input("Pick a number between 1 and 10."))
    if dice_roll == 6:
        level -= 1
        attempts += 1
        print("You are currently on level {0}".format(level))
        dice_roll = int(input("Pick a number between 1 and 10."))
    if dice_roll == 7:
        level -= 1
        attempts += 1
        print("You are currently on level {0}".format(level))
        dice_roll = int(input("Pick a number between 1 and 10."))
    if dice_roll == 8:
        level += 1
        attempts += 1
        print("You are currently on level {0}".format(level))
        dice_roll = int(input("Pick a number between 1 and 10."))
    if dice_roll == 9:
        level += 1
        attempts += 1
        print("You are currently on level {0}".format(level))
        dice_roll = int(input("Pick a number between 1 and 10."))
    if dice_roll == 10:
        level -= 1
        attempts += 1
        print("You are currently on level {0}".format(level))
        dice_roll = int(input("Pick a number between 1 and 10."))
# You win code
    if level == 10:
        play_again = str(print("You win, play again? (y/n)"))
        if play_again == "n":
            print("Have a good day.")
        elif play_again == "y":
            chutes_and_ladders()
        else:
            print("Input either \"y\" or \"n\".")
# You lose code
    if attempts == 20:
        play_again = str(print("You're taking too long, you should just restart, play again? (y/n)"))
        if play_again == "n":
            print("Have a good day.")
        elif play_again == "y":
            chutes_and_ladders()
        else:
            print("Input either \"y\" or \"n\".")
# Run the program
chutes_and_ladders()