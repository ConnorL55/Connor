name = "Connor Le Lievre"
subjects = ["English","History","Science","Algebra","Spanish"]

print("My name is " + name)

print(subjects)

#print(subjects)

for i in subjects:
    print("One of my classes is " + i)


music = ["Bruno Mars", "Cold Play", "Imagine Dragons", "Justin Timberlake"]

for i in music:
    if i == "Bruno Mars":
        print("One of my favorite artists is " + i)
    elif i == "Cold Play":
        print("One of my favorite songs from " + i + "is Paradise")
    else:
        print("I think that " + i + "is a good artist")
    
movies = ["DeadPool", "Maze Runner", "Hunger Games", "It", "Star Wars"]

while True:
    print("What's one of your favorite movies? Type 'end' to quit.")
    answer = input()
    if answer == "end":
       break
    else:
        movies.append(answer)


for i in movies:
    if i == "It":
        print("THATS SCARY!!!")
    elif i == "DeadPool":
        print("Are you excited for DeadPool 2")
        answer = input()
    else:
        print("One of your favorite movies is " + i)
    
