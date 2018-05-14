import pyautogui as pg
import time

points = 0

# Question
answer = pg.prompt(
"""
Which would you rather do?

a) Go out with friends
b) Play video games
c) Relax at home
d) Play sports

"""
    )

# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 2
elif answer == "d":
    points += 1




# Question
answer = pg.prompt(
"""
How offetend do you go out a day?

a) 1
b) 2
c) 3
d) 4

"""
    )

# Give points
if answer == "a":
    points += 4
elif answer == "b":
    points += 3
elif answer == "c":
    points += 2
elif answer == "d":
    points += 1






# Question
answer = pg.prompt(
"""
Where would you rather eat?

a) Go to a restaurant 
b) Eat at home

"""
    )

# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2




# Question
answer = pg.prompt(
"""
How much do you use social media a day?

a) 0 hours
b) 1 hour
c) 2 hours
d) 3 or more hours

"""
    )

# Give points
if answer == "a":
    points += 0
elif answer == "b":
    points += 1
elif answer == "c":
    points += 2
elif answer == "d":
    points += 3



# Question
answer = pg.prompt(
"""
Would you rather?

a) Stay home
b) Go on vacation


"""
    )

# Give points
if answer == "a":
    points += 1
elif answer == "b":
    points += 2

# Introvert
if points >= 8:
    pg.alert("Introvert")
# Extrovert
if points < 8:
    pg.alert("Extrovert")
