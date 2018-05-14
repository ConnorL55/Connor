import random

words = ["youtube","Fortnite","meme","dog"]

hint1 = ["A video site","popular video game","laugh","pet with webbed feet"]

hint2 = ["___tube","Fortnitious","picture with text","barks"]

number = random.randint(0,3)

secretword = words[number]

guess = ""

counter = 0

while True:
    print("Guess the secret word!")
    print("Type 'hint1', 'hint2' or 'give up' for help.")
    guess = input()

    if guess == secretword:
        print("You got it!")
        break

    elif guess == "hint1":
        print( hint1[number] )

    elif guess == "hint2":
        print( hint2[number] )

    elif guess == "give up":
        print("The secret word was " + secretword)
        break
