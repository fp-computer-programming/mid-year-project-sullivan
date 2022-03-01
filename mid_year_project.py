# Author: CRS 02/10/22
# Import Random
import random
# Define the chutes and ladders function
def chutes_and_ladders():
# Create the numbers list
    numbers = [1, 2, 3, 4, 5, 6]
    random.shuffle(numbers)
# Assign level, chutes, ladders, and dice roll variables
    level = 1
    chutes1 = numbers[0]
    chutes2 = numbers[1]
    chutes3 = numbers[2]
    ladders1 = numbers[3]
    ladders2 = numbers[4]
    ladders3 = numbers[5]
    dice_roll = int(input("Pick a number between 1 and 6."))
# Level 1 Code
    if dice_roll == chutes1 & level == 1:
        level = 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == chutes2 & level == 1:
        level = 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == chutes3 & level == 1:
        level = 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == ladders1 & level == 1:
        level += 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == ladders2 & level == 1:
        level += 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == ladders3 & level == 1:
        level += 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
# Level 2 Code
    if dice_roll == chutes1 & level == 2:
        level -= 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == chutes2 & level == 2:
        level -= 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == chutes3 & level == 2:
        level -= 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == ladders1 & level == 2:
        level += 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == ladders2 & level == 2:
        level += 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == ladders3 & level == 2:
        level += 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
# Level 3 Code
    if dice_roll == chutes1 & level == 3:
        level -= 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == chutes2 & level == 3:
        level -= 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == chutes3 & level == 3:
        level -= 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == ladders1 & level == 3:
        level += 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == ladders2 & level == 3:
        level += 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == ladders3 & level == 3:
        level += 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
# Level 4 Code
    if dice_roll == chutes1 & level == 4:
        level -= 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == chutes2 & level == 4:
        level -= 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == chutes3 & level == 4:
        level -= 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == ladders1 & level == 4:
        level += 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == ladders2 & level == 4:
        level += 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == ladders3 & level == 4:
        level += 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
# Level 5 Code
    if dice_roll == chutes1 & level == 5:
        level -= 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == chutes2 & level == 5:
        level -= 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == chutes3 & level == 5:
        level -= 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == ladders1 & level == 5:
        level += 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == ladders2 & level == 5:
        level += 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == ladders3 & level == 5:
        level += 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
# Level 6 Code
    if dice_roll == chutes1 & level == 6:
        level -= 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == chutes2 & level == 6:
        level -= 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == chutes3 & level == 6:
        level -= 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == ladders1 & level == 6:
        level += 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == ladders2 & level == 6:
        level += 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == ladders3 & level == 6:
        level += 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
# Level 7 Code
    if dice_roll == chutes1 & level == 7:
        level -= 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == chutes2 & level == 7:
        level -= 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == chutes3 & level == 7:
        level -= 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == ladders1 & level == 7:
        level += 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == ladders2 & level == 7:
        level += 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == ladders3 & level == 7:
        level += 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
# Level 8 Code
    if dice_roll == chutes1 & level == 8:
        level -= 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == chutes2 & level == 8:
        level -= 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == chutes3 & level == 8:
        level -= 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == ladders1 & level == 8:
        level += 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == ladders2 & level == 8:
        level += 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == ladders3 & level == 8:
        level += 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
# Level 9 Code
    if dice_roll == chutes1 & level == 9:
        level -= 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == chutes2 & level == 9:
        level -= 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == chutes3 & level == 9:
        level -= 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == ladders1 & level == 9:
        level += 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == ladders2 & level == 9:
        level += 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
    if dice_roll == ladders3 & level == 9:
        level += 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))
# You win code
    if level == 10:
        play_again = str(print("You win, play again? (y/n)"))
        if play_again == "n":
            print("Have a good day.")
        elif play_again == "y":
            chutes_and_ladders()
        else:
            print("Input either \"y\" or \"n\".")

# Run the program
chutes_and_ladders()

"""
    elif dice_roll == chutes1 & level != 1:
        level -= 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))

    elif dice_roll == chutes2 & level != 1:
        level -= 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))

    elif dice_roll == chutes3 & level != 1:
        level -= 1
        print("You are currently on level {0}".format(level))
        random.shuffle(numbers)
        dice_roll = int(input("Pick a number between 1 and 6."))


"""