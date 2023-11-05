from PIL import Image
import os

letters = ['a', 'f', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters += [letter.capitalize() for letter in letters]

usedLetters = []

def readSheet(source):
    images = []

    image = Image.open(source)
    loaded = image.load()

    w = 100
    h = 80

    colors = []
    for r in range(3):
        images.append([])
        for c in range(8):
            images[-1].append([])
            for y in range(h*r, h*r+h):
                images[-1][-1].append([])
                for x in range(w*c, w*c+w):
                    color = loaded[x,y]
                    if color[3] != 255:
                        color = BLACK
                    if color[:3] not in colors:
                        colors.append(color[:3])
                    images[-1][-1][-1].append(colors.index(color[:3]))
        
    return images, colors

def stringify(line):
    line = str(line)
    for i, letter in enumerate(usedLetters):
        line = line.replace(str(i+10), letter)
    return line

def writeFile(images, colors, dest):
    for i in range(len(colors)-10):
        if i < len(letters):
            usedLetters.append(letters[i])

    f = open(dest, 'w+')

    if len(usedLetters) > 0:
        f.write(", ".join(usedLetters) + " = " + ", ".join([i+10 for i in range(len(usedLetters))]))
    f.write("colors = " + str(colors) + "\n\n")

    f.write("[\n")
    for row in images:
        f.write("    [\n")
        for image in row:
            f.write("        [\n")
            for line in image:
                f.write("            " + stringify(line).replace(' ', '') + ",\n")
            f.write("        ],\n")
        f.write("    ],\n")
    f.write("]")

    f.close()

if __name__ == "__main__":
    source = "/Users/andrewfox/Documents/Game/Assets/Prototype Hero Demo/Sprites/PrototypeHero_noSword.png"#input("image file path: ")
    images, colors = readSheet(source)
    dest = "bitmaps/temp.py"#input("destination file path: ")
    writeFile(images, colors, dest)