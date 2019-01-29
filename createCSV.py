#creates a cv file for a game film
# 0 is no possession
# 1 is celtics
# 2 is warriors

import csv

path = "film_3"
name = path + "/mapping.csv"

#array of pairs that describe who has the ball when
#(0,1) means at frame 0, celtics have the ball
#need to note any change in possession and possesion at the first and last + 1 frames
array = [(0,1),(10,0),(15,2),(20,2)]


with open (name,"w") as csvfile:
    filewriter = csv.writer(csvfile,delimiter=",",quotechar="|",quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(["Image_ID","Class"])
    for i in range(len(array)-1):
        for j in range(array[i][0],array[i+1][0]):
            image = "frame" + str(j) + ".jpg"
            filewriter.writerow([image,array[i][1]])
