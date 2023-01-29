import random


def int_input(inputMessage):
    return int(input(inputMessage))


print("Guess a number between 1 and 25")
inputNumber = int_input("Please enter a number: ")
number = random.randint(1, 25)
while(inputNumber != number):
    if(number > inputNumber):
        inputNumber = int_input("Increase your number: ")
    else:
        inputNumber = int_input("Decrease your number: ")

print("You won !")
