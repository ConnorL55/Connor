import random
import time

number = random.randint(1,100)

guess = 0

counter = 0

while True:
    counter += 1
    print("Guess my number 1-100! It is a whole number")
    guess = int(input())   

    if guess == number:
        print("You got it!")
        print("You took " + str(counter) + " guesses.")
        break
    
    elif guess > number:
        print("Woah that was too big")
        

    elif guess < number:
        print("Too low! Try again.")
        
