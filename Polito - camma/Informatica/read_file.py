FILENAME = "story.txt"
file = open(FILENAME,"r")

voti = [float(row) for row in file ]

if len(voti) != 0:
    print("La media è ", sum(voti)/len(voti))
file.close()
