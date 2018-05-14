### MAD LIBS ###
import time 
print("Give me a name")
name1 = input()

print("Give me another name")
name2 = input()

print("Give me a verb ending in ing")
verb1 = input()

print("Give me a place")
place1 = input()

print("Give me an adjective")
adj1 = input()

print("Give me a second adjective")
adj2 = input()
### Begin Mad Lib ###

print("Hey " + name1 + ", How's it going " + name2 + " said")

print("'I am fine' " + name1 + " said")

print("'You look tired have you been " + verb1 +"' " + name2 + " asked")

print("I went down to " + place1 + " and went " + verb1 + " " + name1 + " replied")

print("'Cool' " + name2 + " said")

print("'What did you think of the science test'" +  name1 + " asked")

print("'I thought it was so " + adj1 +"'" + name2 + " said")

print("'I totally disagree I think it was so " + adj2 + "'" + name1 + " said angerly")

time.sleep(100)
