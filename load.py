from PIL import Image
import numpy as np
asciiS = " .,:irs?@9B&#"#"`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$""`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
#print(len(asciiS))
#im = Image.open("2rgh5r.jpg")
#im = Image.open("iron-man.jpg")
#im = Image.open("tt0060196.jpg")
#im = Image.open("tt0068646.jpg")
#im = Image.open("tt0083866.jpg")
#im = Image.open("tt0974015.jpg")
im = Image.open("tt2911666.jpg")
size = 200,200
im.thumbnail(size, Image.ANTIALIAS)
#print(im.format, im.size, im.mode)
iar = np.asarray(im)
print(iar.max())
#print(iar)
#print(iar.shape)
height = len(iar)
width = len(iar[0])
brightness = np.zeros((height, width))
for x in range(height):
    for y in range(width):
        r = int(iar[x][y][0])
        g = int(iar[x][y][1])
        b = int(iar[x][y][2])
        brightness[x][y] = (r+g+b)/3 #0.21*r + 0.72*g + 0.07*b#
scaledA = np.zeros((height, width))
#f = open('workfile', 'w')
for x in range(height):
    for y in range(width):
        brightnessVal = brightness[x][y]
        scaledA = asciiS[int(brightnessVal*(len(asciiS)-1)/255)]
        #scaledA = asciiS[int(brightnessVal*len(asciiS)/255)-1]
        print(scaledA+scaledA+scaledA, end='')
        #f.write(scaledA+scaledA+scaledA)
    print("\n")
    #f.write("\n")
#f.close()
#ime = Image.fromarray(np.asarray(scaledA))
#ime.show()