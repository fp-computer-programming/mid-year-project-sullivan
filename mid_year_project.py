# Author: CRS 02/10/22

# Define the chutes and ladders function

def chutes_and_ladders(roll1, roll2, roll3, roll4, roll5, roll6, roll7, roll8, roll9, roll10):

# Assign level, dice roll, and attempts variable

    level = 0

# Dice roll code

    level = roll1 + roll2 + roll3 + roll4 + roll5 + roll6 + roll7 + roll8 + roll9 + roll10

# You win code

    if level >= 10:
        
        print("You win!")

        print("Have a good day.")

# You lose code

    else:

        print("You lose.")

        print("Have a good day.")

# Test 1

chutes_and_ladders(3, -1, 6, 5, -2, 10, 7, 8, -4, 9)

# Test 2

chutes_and_ladders(-9, -5, 6, 1, 3, 4, -7, -10, 8, 2)

# Test 3

chutes_and_ladders(1, -2, 3, 4, 5, 6, 7, 8, 9, 10)
    
# Survey

survey = input("Would you like to take a brief survey about your experience?")

print("I don't have code to accept yes or no, you're taking it either way.")

# Rating

rating = input("Please rate this game out of 5 stars.")

print("Thanks for your feedback!")

# Question 1

question1 = input("Would you have been able to get this code to 100 lines?")

# If you said yes

yes = "If you said yes, good for you."

print(yes)

# If you said no

no = "If you said no, at least I know I'm not alone."

print(no)

# Question 2

question2 = input("Would you like some life advice?")

# Don't care

dont_care = "Well you're getting it either way."

print(dont_care)

# Life advice

life_advice = "Do your project before it's too late."

print(life_advice)

# Question 3

question3 = input("Would you like more advice?")

# More advice

more_advice = "Don't try to make chutes and ladders in python, it doesn't work."

print(more_advice)

# Thanks for watching

thanks_for_watching = "Thanks for watching."

print(thanks_for_watching)
