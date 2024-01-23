import random

randomSelector = random.randint(1,2)

userInput = int(input("Welcome to the Grand Coin toss game! Chose your 1 for heads or 2 for tails: "))
if userInput == randomSelector:
    print("You won the game!")
else:
    print("You lost!")

#This is my simple coin toss game I created! Enjoy!
