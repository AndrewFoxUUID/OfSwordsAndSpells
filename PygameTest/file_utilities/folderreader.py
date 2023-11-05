from PIL import Image
import os

letters = ['a', 'f', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters += [letter.capitalize() for letter in letters]

usedLetters = []

def findColor(c, colors):
    for i, color in list(enumerate(colors))[1:]:
        if abs(c[0] - color[0]) < 5 and abs(c[1] - color[1]) < 5 and abs(c[2] - color[2]) < 5:
            return max(i-1,0)
    colors.append(c)
    return max(len(colors)-2,0)

def readFolder(source):
    firstRow = WW
    lastRow = 0
    firstCol = WW
    lastCol = 0
    images = {}
    colors = [None]
    for file in os.listdir(source):
        if file != '.DS_Store':
            images[file] = []

            image = Image.open(source + "/" + file)
            loaded = image.load()

            for y in range(image.size[1]):
                images[file].append([])
                for x in range(image.size[0]):
                    color = loaded[x,y]
                    if color[3] != 255:
                        color = None
                    else:
                        color = color[:3]
                    #i = findColor(color[:3], colors)
                    if color in colors:
                        i = colors.index(color)
                    else:
                        colors.append(color)
                        i = len(colors) - 1
                    #if i != 0:
                        #if y < firstRow:
                        #    firstRow = y
                        #if y > lastRow:
                        #    lastRow = y
                        #if x < firstCol:
                        #    firstCol = x
                        #if x > lastCol:
                        #    lastCol = x
                    images[file][-1].append(i)
                    #images[file][-1].append(color)
        
    return images, colors#, [firstRow, lastRow, firstCol, lastCol]

def stringify(line):
    line = str(line)
    for i, letter in enumerate(usedLetters):
        line = line.replace(str(i+10), letter)
    return line

def writeFile(images, colors, dest):#, dims):
    for i in range(len(colors)-10):
        if i < len(letters):
            usedLetters.append(letters[i])

    f = open(dest, 'w+')

    f.write("colors = " + str(colors) + "\n\n")

    for file in images:
        f.write(file[:file.index('.')].replace('-', '_') + " = [\n")
        for line in images[file]:#[dims[0]:dims[1]+1]:
            f.write("    " + stringify(line).replace(' ', '') + ",\n")#[dims[2]:dims[3]+1]
        f.write("]\n")

    f.close()

if __name__ == "__main__":
    source = "Assets Store/16x16 RPG Item Pack"#input("source folder path: ")
    images, colors = readFolder(source)#, dims
    dest = "bitmaps/temp.py"#input("destination file path: ")
    writeFile(images, colors, dest)#, dims)