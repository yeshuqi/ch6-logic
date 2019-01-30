# This script contains a program for a simple guessing game!

# Define a function `print_hot_or_cold()` that takes in two arguments (the 
# `target` and the `guess`), and prints out an appropriate message based on 
# how close the guess is to the target:
#
# Distance    Message
# -------------------
# The same    "got it!"
# Within 1	  "scalding hot"
# Within 3	  "very warm"
# Within 5	  "warm"
# Within 8	  "cold"
# Within 13	  "very cold"
# > 13 away	  "icy freezing miserably cold"
#
# Be sure to consider both positive AND negative distances!
# BONUS: Also print out whether the guess is high or low
def print_hot_or_cold(target, guess):
    dis = abs(target - guess)
    if dis == 0:
       print("got it")
    elif dis <= 1:
       print("scalding hot")
    elif dis <= 3 and dis > 1:
       print("very warm")
    elif dis <= 5 and dis > 3:
       print("warm")
    elif dis <= 8 and dis > 5:
       print("cold")
    elif dis <= 13 and dis > 8:
       print("very cold")
    elif dis > 13:
       print("icy freezing miserably cold")
    if target > guess:
        print("guess is low")
    elif target < guess:
        print("guess is high")

# Define a function `guess_number()` that takes a single argument (a target number)
# and prompts the user for a guess using the `input()` method. Your function should
# then print how close the user's guess is to that target (use your previous 
# function!). Note that you will need to convert the input into a number.
#
# Once you have a single guess working, modify your function so that the user can
# make MULTIPLE guesses. You can either do this using a loop (see the next chapter)
# or by simply calling your `guess_number() method again IF the user didn't get
# the answer right. The later is an example of **recursion**.
def guess_number(target):
    guess = int(input("Guess a number: "))
    print_hot_or_cold(target, guess)
    if guess != target:
        guess_number(target)
guess_number(50)
# If the file is run as a top-level script, your script should pick a random number
# between 1 and 50 as the target and then start the game. You should inform the
# user of the range of numbers before asking them for a guess.
if __name__ == "__main__":
    import random
    target = random.randint(1,50)
    print("Try picking a number")
    guess_number(target)