# End Portal location calculator, based on location of end portal in the first ring of end portals

import math

#This is the text file the Coords are output to
output = open("Server Portal Coords.txt", "a")

c = True

while c == True:
# variables for coords of the first portal in a circle you find
    x11 = int(input("X coordinate: "))
    z11 = int(input("Z coordinate: "))

#distance from 0,0 (radius)
    r1 = int(math.sqrt((x11**2 + z11**2)))

#variables for which circle, the minimum distance from 0,0, the amount of portals in each circle, and the angle of seperation between each portal
    circle = int(10)
    minrad = [1280, 4352, 7424, 10496, 13568, 16640, 19712, 22784]
    pcount = [3, 6, 10, 15, 21, 28, 36, 9]
    angle = [120, 60, 36, 24, (360/21), (360/28), 10, 40]

#finds which circle you are in
    if 1279 < r1 < 2817:
        circle = int(0)
        c = False
    elif 4351 < r1 < 5889:
        circle = int(1)
        c = False
    elif 7423 < r1 < 8961:
        circle = int(2)
        c = False
    elif 10495 < r1 < 12033:
        circle = int(3)
        c = False
    elif 13567 < r1 < 15105:
        circle = int(4)
        c = False
    elif 16639 < r1 < 18177:
        circle = int(5)
        c = False
    elif 19711 < r1 < 21249:
        circle = int(6)
        c = False
    elif 22783 < r1 < 24321:
        circle = int(7)
        c = False
    else:
        print("Invalid Coordinates")


#finds the angle from the postitive x-axis
a11 = (math.degrees(math.atan2(z11, x11)))
if a11 < 0:
    a11 = 360 + a11

#writes the circle number to the text file
cout = ("\n" + "Circle Number: " + str(circle + 1) + "\n")
output.write(cout)

#variables for finding aproximate portal locations
t = pcount[circle]
s = 1
a = a11

#variable for writing portal coords to document
pout = str()


while t > 0:
#finding nether portal coords
    x = x11/8
    z = z11/8
#combining data into a string to write to the text document
    pout = (str(s) + "  X: " + str(int(x11)) + "    Z: " + str(int(z11)) + "    X nether: " + str(int(x)) + "   Z nether: " + str(int(z)) + "\n")
#printing and writing to the console and document
    print(pout)
    output.write(pout)
#getting the portal number
    s = s + 1
#finding the angle from the positive x-axis and calculating coordinates
    a = a + angle[circle]
    x11 = (minrad[circle] + 768) * math.cos(math.radians(a))
    z11 = (minrad[circle] + 768) * math.sin(math.radians(a))
    t = t - 1

    output.close()