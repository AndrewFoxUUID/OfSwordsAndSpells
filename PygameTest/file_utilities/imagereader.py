from PIL import Image
import os

letters = ['a', 'f', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters += [letter.capitalize() for letter in letters]

def readImage(source):
    mat = []
    colors = []

    image = Image.open(source)
    loaded = image.load()

    for y in range(0, image.size[1]):
        line = []
        for x in range(0, image.size[0]):
            color = loaded[x,y][:3]
            if color not in colors:
                colors.append(color)
            line.append(colors.index(color))
        mat.append(line)

    return mat, colors

def readGif(source):
    frames = []
    colors = []

    gif = Image.open(source)
    for i in range(gif.n_frames):
        gif.seek(i)
        loaded = gif.convert("RGB")

        frames.append([])
        for y in range(0, loaded.size[1]):
            frames[-1].append([])
            for x in range(0, loaded.size[0]):
                r, g, b = loaded.getpixel((x, y))
                color = (r, g, b)
                if color not in colors:
                    colors.append(color)
                frames[-1][-1].append(colors.index(color))
    
    return frames, colors

def findColor(c, colors):
    for i, color in list(enumerate(colors))[1:]:
        if abs(c[0] - color[0]) < 5 and abs(c[1] - color[1]) < 5 and abs(c[2] - color[2]) < 5:
            return i, color;
    return len(colors), c

def join(lst):
    if len(lst) > 0:
        joined = str(lst[0])
        for item in lst[1:]:
            joined += ", " + str(item)
        return joined
    else:
        return ""

def enhance(mat, colors):
    p = 3 #4
    newcolors = [BLACK]
    newmat = []
    for y in range(int(len(mat)/p)):
        newmat.append([])
        for x in range(int(len(mat[0])/p)):
            if p == 4:
                topleft = mat[y*4+1][x*4+1]
                topright = mat[y*4+1][x*4+2]
                bottomleft = mat[y*4+2][x*4+1]
                bottomright = mat[y*4+2][x*4+2]
                color = (
                    int((colors[topleft][0] + colors[topright][0] + colors[bottomleft][0] + colors[bottomright][0]) / 4),
                    int((colors[topleft][1] + colors[topright][1] + colors[bottomleft][1] + colors[bottomright][1]) / 4),
                    int((colors[topleft][2] + colors[topright][2] + colors[bottomleft][2] + colors[bottomright][2]) / 4)
                )
            elif p == 3:
                color = colors[mat[y*3+1][x*3+1]]
            index, color = findColor(color, newcolors)
            if index == len(newcolors):
                newcolors.append(color)
            newmat[-1].append(index)
    newcolors[0] = None
    return newmat, newcolors

def readDirToFile():
    source = input("source: ")
    target = input("target: ")
    steps = int(input("steps: "))

    lines = []
    colors = []

    lines.append("colors = " + str(colors) + "\n")
    lines.append("frames = [\n")
    for i in range(1, 49):
        lines.append("    [\n")
        image = Image.open(source + str(i) + ".png")
        loaded = image.load()
        grid = []

        for x in range(0, image.size[0], steps):
            for y in range(0, image.size[1], steps):
                if int(y/steps) >= len(grid):
                    grid.append([])
                color = img[x,y]
                if color not in colors:
                    colors.append(color)
                grid[int(y/steps)].append(colors.index(color))

        for row in grid:
            lines.append("        " + str(row).replace(" ", "") + ",\n")

        lines.append("    ],\n")
    lines.append("]")
    lines[0] = "colors = " + str(colors) + "\n"

    f = open(target, "w")
    for line in lines:
        f.write(line)
    f.close()

def readGifToFile():
    source = "images/giftest.gif"#input("source: ")
    gif = Image.open(source)
    target = "worlds/gif.py"#input("target: ")
    steps = 4#int(input("pixels/pixel: "))
    startx = 26#int(input("startx: "))
    endx = 158#int(input("endx: "))
    starty = 26#int(input("starty: "))
    endy = 116#int(input("endy: "))
    eliminate = ['1','2','4','5','A','B']

    lines = []
    extras = []
    colors = []

    lines.append("colors = " + str(colors) + "\n")
    lines.append("frames = [\n")
    for i in range(gif.n_frames):
        lines.append("    [\n")
        gif.seek(i)
        loaded = gif.convert("RGB")

        grid = []

        for y in range(starty*4, endy*4, 4):
            line = []
            for x in range(startx*4, endx*4, 4):
                r, g, b = loaded.getpixel((x, y))
                color = (r, g, b)
                if color not in colors:
                    colors.append(color)
                line.append(colors.index(color))
            line = str(line)
            for j in range(10, len(colors)):
                if j-10 >= len(letters):
                    break
                if str(j) in line and letters[j-10] not in extras:
                    extras.append(letters[j-10])
                line = line.replace(str(j), letters[j-10])
            for char in eliminate:
                line = line.replace(char, "0")
            lines.append("        " + line.replace(" ", "") + ",\n")

        lines.append("    ],\n")
    lines.append("]")
    colors[0] = WHITE
    lines[0] = "colors = " + str(colors) + "\n"
    if len(extras) != 0:
        line = extras[0]
        for extra in extras[1:]:
            line += ", " + extra
        line += " = 10"
        for i in range(len(extras[1:])):
            line += ", " + str(i+11)
        line += "\n"
        lines.insert(0, line)

    f = open(target, "w")
    for line in lines:
        f.write(line)
    f.close()

def drawToFile(grid, colors):

    exclude = []

    lines = ["image = [\n"]

    for row in grid:
        if type(row[0]) == list:
            lines.append("    [\n")
            for line in row:
                lines.append("        " + str(line).replace(" ", "") + ",\n")
            lines.append("    ],\n")
        else:
            lines.append("    " + str(row).replace(" ", "") + ",\n")
    
    excluded = 0
    for i in list(range(len(colors)))[1:]:
        if i in exclude:
            excluded += 1
            for j in range(len(lines)):
                lines[j] = lines[j].replace(',' + str(i) + ',', ',0,').replace('[' + str(i) + ',', '[0,').replace(',' + str(i) + ']', ',0]')
                lines[j] = lines[j].replace(',' + str(i) + ',', ',0,').replace('[' + str(i) + ',', '[0,').replace(',' + str(i) + ']', ',0]')
        else:
            new = str(i - excluded)
            for j in range(len(lines)):
                lines[j] = lines[j].replace(',' + str(i) + ',', ',' + new + ',').replace('[' + str(i) + ',', '[' + new + ',').replace(',' + str(i) + ']', ',' + new + ']')
                lines[j] = lines[j].replace(',' + str(i) + ',', ',' + new + ',').replace('[' + str(i) + ',', '[' + new + ',').replace(',' + str(i) + ']', ',' + new + ']')

    for i in exclude[::-1]:
        colors.pop(i)
    lines.insert(0, "colors = " + str(colors) + "\n")
    
    lines.append("]")

    if len(colors) > 10:
        extras = []
        extranums = []
        for i in range(len(colors)-10):
            if i < len(letters):
                letter = letters[i]
            else:
                letter = chr(i + 71)
            extras.append(letter)
            extranums.append(i + 10)
            for j in range(1, len(lines)):
                lines[j] = lines[j].replace(str(i+10), letter)
        lines.insert(0, join(extras) + " = " + join(extranums) + "\n")

    f = open("bitmaps/temp.py", "w")
    for line in lines:
        f.write(line)
    f.close()

if __name__ == "__main__":
    #image, colors = readImage(input("source: "))
    image, colors = readGif(input("source: "))
    drawToFile(image, colors)