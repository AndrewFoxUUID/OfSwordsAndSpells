from utilityclasses import *

a, b, c = 10, 11, 12

world1colors = [None, (20, 160, 46), (40, 92, 196), (26, 122, 63), (36, 160, 222), (36, 82, 59), (185, 191, 251), (64, 51, 81), (71, 125, 133), (227, 230, 255), (88, 141, 190), (66, 57, 52), (59, 23, 37)]
world1 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,3,3,3,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,3,3,1,3,3,3,3,3,4,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,3,3,3,3,3,3,3,4,4,4,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,3,3,3,3,3,5,5,3,3,4,4,4,4,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,1,1,3,1,1,3,3,3,3,3,5,5,5,5,5,5,5,4,4,2,4,4,4,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,1,1,3,3,3,3,5,5,3,5,5,5,6,6,6,5,4,4,4,2,2,4,4,4,2,2,2,2,2,7,7,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,1,1,3,3,3,3,5,5,6,6,5,5,5,6,6,5,5,5,4,4,4,4,2,8,8,4,2,2,2,2,2,2,7,7,0,0,0,0,0,0],
    [0,0,0,0,0,0,6,1,1,3,3,3,3,5,6,6,6,5,5,5,6,9,9,9,6,4,4,4,4,4,a,a,2,4,2,2,2,2,2,2,7,7,0,0,0,0,0,0],
    [0,0,0,0,0,9,9,9,9,3,3,5,5,6,9,9,6,5,6,9,9,9,9,9,9,4,4,4,4,9,9,a,2,2,2,2,2,2,2,2,7,7,6,0,0,0,0,0],
    [0,0,0,0,9,9,9,9,6,3,5,6,6,9,9,9,9,9,9,9,9,9,9,9,9,6,4,9,9,9,6,4,2,2,2,2,2,2,2,7,2,7,6,a,0,0,0,0],
    [0,0,0,9,9,9,9,6,3,3,5,9,9,9,9,9,9,9,9,9,6,6,6,9,6,4,4,9,9,6,4,4,6,6,2,1,3,3,3,2,7,2,6,a,a,0,0,0],
    [0,0,0,9,9,9,9,6,9,9,9,9,9,9,9,9,9,9,9,6,4,4,4,4,4,4,4,4,4,4,4,6,6,1,1,1,1,3,3,3,7,6,a,a,a,0,0,0],
    [0,0,a,9,9,9,9,9,9,9,6,9,9,9,9,9,9,9,9,6,6,6,4,4,4,4,4,4,4,4,6,6,9,1,1,1,1,3,3,3,3,a,a,a,a,8,0,0],
    [0,0,2,9,9,9,9,9,9,9,6,9,9,9,9,9,9,9,9,9,6,4,4,4,4,4,4,4,4,9,9,9,1,1,1,3,1,3,3,3,3,b,b,a,a,8,0,0],
    [0,2,4,4,6,6,6,9,9,9,9,6,6,6,4,6,9,9,9,4,4,4,4,4,4,4,4,4,1,1,1,1,1,1,1,1,3,3,3,3,3,b,a,a,a,8,8,0],
    [0,2,4,4,4,4,4,4,4,4,6,6,4,4,4,6,6,6,6,4,4,4,4,4,4,4,4,4,1,1,1,1,1,1,1,1,3,3,3,3,6,6,a,a,a,8,8,0],
    [0,2,4,4,4,4,3,3,6,6,4,4,4,4,4,4,6,6,6,6,4,4,4,4,4,4,4,4,4,1,1,1,3,3,1,3,3,5,5,6,a,a,a,a,8,8,8,0],
    [0,2,4,4,4,3,3,1,b,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,1,3,1,1,3,3,3,3,3,3,5,a,a,8,8,8,8,8,0],
    [2,2,2,4,4,b,1,b,6,9,6,6,4,4,4,4,4,4,4,4,4,9,4,4,4,4,4,4,4,3,3,1,3,3,3,3,3,3,6,a,a,a,a,a,8,8,7,7],
    [2,2,2,4,4,4,b,6,9,9,9,4,4,4,4,4,4,4,4,4,6,4,4,4,4,4,4,4,4,1,3,3,3,3,3,5,3,6,6,6,a,a,a,a,7,7,7,7],
    [2,2,2,2,4,4,a,6,4,4,4,4,4,4,4,4,4,4,4,9,6,4,4,4,4,4,4,4,6,4,1,3,5,3,3,5,5,a,a,a,a,b,b,b,7,7,7,7],
    [2,2,2,2,2,4,a,6,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,6,6,4,4,6,4,4,4,3,3,5,5,5,5,5,a,a,2,b,b,b,7,7,7,7],
    [2,2,2,2,4,4,4,6,6,4,4,4,4,4,4,4,4,4,4,4,4,4,6,4,4,4,4,6,6,4,4,4,3,5,5,5,5,b,b,a,a,2,7,7,7,7,7,7],
    [2,2,2,4,4,4,4,4,9,9,4,4,4,4,4,4,4,4,4,6,4,4,6,9,9,4,4,4,9,6,4,4,4,3,3,5,b,b,b,b,b,2,7,7,7,7,7,7],
    [2,2,2,4,4,9,4,4,4,4,4,4,4,4,4,4,4,4,6,4,4,6,9,9,9,6,4,9,9,9,4,4,2,3,5,5,b,b,b,b,b,7,7,7,7,7,7,7],
    [2,2,2,4,a,9,9,6,4,4,6,6,6,4,4,4,4,6,4,6,9,9,9,9,9,9,9,9,9,6,4,2,2,2,5,b,b,b,b,b,b,2,7,7,7,7,7,7],
    [2,2,2,4,a,9,9,9,6,6,9,4,4,4,4,4,6,9,6,9,9,9,9,9,9,9,9,9,9,6,2,2,2,4,2,5,b,b,b,2,7,7,7,7,7,7,7,7],
    [2,2,2,2,4,a,9,9,9,9,9,9,6,6,4,6,9,9,9,9,9,9,9,9,9,9,9,9,9,a,a,2,2,2,2,2,2,2,2,7,2,7,7,7,7,7,7,7],
    [0,2,2,2,2,4,a,9,9,9,a,9,9,9,9,9,9,9,9,9,9,9,9,9,a,9,9,a,a,a,a,2,2,2,2,2,2,2,7,2,a,7,7,7,7,7,7,0],
    [0,2,2,2,2,2,2,a,a,a,a,9,9,6,9,9,9,9,9,9,9,a,9,a,a,a,a,a,a,a,a,2,2,2,2,2,7,2,7,a,a,7,7,7,7,7,7,0],
    [0,2,2,2,2,2,2,2,a,2,a,a,a,a,9,9,9,9,9,9,a,4,2,a,a,a,a,a,a,a,5,2,2,2,2,7,2,a,a,a,8,8,7,7,7,7,7,0],
    [0,2,2,2,2,2,2,2,2,2,3,b,b,a,a,a,9,9,a,a,a,a,2,2,2,a,a,a,a,5,5,5,5,a,7,a,a,a,a,a,8,8,8,7,7,7,7,0],
    [0,0,2,2,2,2,2,2,2,b,5,5,b,2,a,a,a,a,a,a,a,a,2,2,2,5,5,5,5,5,5,5,a,c,a,a,a,a,8,8,8,8,7,7,7,7,0,0],
    [0,0,2,2,2,2,2,2,2,2,b,b,2,2,a,a,a,a,2,2,a,a,2,2,5,5,5,5,5,5,5,a,5,a,a,a,a,a,8,8,8,7,7,7,7,7,0,0],
    [0,0,0,2,2,2,2,2,2,2,2,2,a,a,a,2,2,2,2,2,2,2,2,2,5,5,5,5,b,b,b,a,a,a,8,8,8,8,8,7,7,7,7,7,7,0,0,0],
    [0,0,0,2,2,2,2,2,2,2,2,2,2,a,a,a,2,2,2,2,2,2,2,2,5,5,5,b,b,a,b,c,a,a,a,a,8,c,7,7,7,7,7,7,7,0,0,0],
    [0,0,0,0,2,2,2,2,2,2,2,2,2,2,a,a,a,a,2,5,5,5,2,2,5,5,5,b,a,c,b,a,a,a,a,8,8,8,8,8,7,7,7,7,0,0,0,0],
    [0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,5,5,5,5,5,2,7,5,5,b,a,a,a,a,8,a,8,8,8,8,c,c,7,7,7,0,0,0,0,0],
    [0,0,0,0,0,0,7,2,7,2,2,2,2,2,2,2,2,5,5,5,5,5,5,5,7,5,5,a,a,a,a,a,8,8,8,8,8,8,c,c,c,c,0,0,0,0,0,0],
    [0,0,0,0,0,0,7,7,2,7,2,7,2,7,2,c,5,5,5,5,b,b,b,5,5,c,5,a,a,a,8,8,8,8,8,8,8,c,c,c,c,c,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,7,7,2,7,2,7,c,5,5,c,5,5,b,c,b,c,5,c,5,c,5,b,8,8,8,8,8,c,c,c,c,c,c,c,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,c,c,c,c,5,c,c,5,c,b,c,b,c,b,c,5,c,c,c,c,c,c,c,c,c,c,c,c,c,c,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,c,c,c,c,c,c,c,c,c,c,b,c,b,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,c,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,c,c,c,c,c,c,c,c,c,c,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

world2colors = [None, (233, 235, 255), (185, 191, 251), (88, 141, 190), (179, 185, 209), (102, 119, 158), (119, 130, 173)]
world2 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,2,3,3,2,2,1,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,2,3,3,4,3,2,2,1,2,2,2,2,2,2,2,3,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,2,2,2,2,2,1,1,1,1,2,2,2,2,2,3,5,5,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,3,3,5,5,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,4,4,4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,3,3,5,5,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,1,1,1,1,4,4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,3,3,5,5,6,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,3,5,5,5,6,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,3,5,5,3,0,0,0,0,0,0],
    [0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,3,5,3,3,6,0,0,0,0,0],
    [0,0,0,0,1,1,1,1,1,1,2,2,2,2,3,3,3,3,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,3,3,4,4,3,3,6,0,0,0,0],
    [0,0,0,1,1,1,1,1,1,2,2,2,3,1,1,3,3,2,2,2,1,1,1,1,4,4,1,1,1,1,1,1,1,1,1,2,2,3,4,4,4,3,3,6,6,0,0,0],
    [0,0,0,1,1,1,1,1,1,2,2,3,1,1,1,3,2,2,1,1,1,1,1,1,1,4,4,4,1,2,1,1,1,1,2,2,2,3,3,4,3,3,6,6,6,0,0,0],
    [0,0,1,1,1,1,1,1,1,1,2,2,3,1,2,2,1,1,1,1,1,1,1,1,1,1,4,4,1,1,2,1,1,1,2,2,2,2,3,3,3,2,6,6,6,6,0,0],
    [0,0,1,1,1,1,1,1,1,1,1,2,2,3,2,1,1,1,1,1,4,1,1,1,1,4,4,1,1,1,1,2,1,1,1,1,2,2,2,2,2,2,6,6,6,6,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,2,3,2,1,1,1,1,1,1,4,4,4,4,4,4,1,1,1,1,2,1,1,1,1,2,2,2,2,2,6,2,6,6,6,6,0],
    [0,1,1,1,1,1,1,4,1,1,1,1,3,3,2,1,1,1,1,1,1,1,4,4,4,1,1,1,1,1,1,2,3,1,1,1,1,2,2,2,2,2,6,6,6,6,6,0],
    [0,1,1,1,1,1,4,4,1,1,1,1,3,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,3,3,1,1,1,1,2,2,2,2,2,6,6,6,6,6,0],
    [0,1,1,1,1,1,4,4,1,1,1,2,3,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,2,2,1,1,2,2,2,2,2,6,2,6,6,6,6,0],
    [2,2,1,1,1,1,4,1,1,1,1,2,3,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,6,6,6,6,6,6],
    [2,2,1,1,1,1,1,1,1,1,1,1,2,3,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,6,6,6,6,6,6],
    [2,2,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,2,2,2,1,1,1,1,1,1,2,3,2,2,2,2,2,2,6,2,6,6,6,6,6],
    [2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,1,4,1,1,2,2,2,2,1,1,1,1,2,2,3,2,2,2,2,2,2,6,2,6,6,6,6,6,6],
    [2,2,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,4,4,4,1,1,1,2,2,3,2,2,1,1,1,1,1,2,1,2,2,2,2,2,6,2,6,6,6,6,6,6],
    [2,2,2,2,1,1,1,1,1,2,1,1,1,1,1,1,4,1,4,1,1,1,1,1,2,2,3,2,2,1,1,1,1,1,1,2,2,2,2,6,2,6,6,6,6,6,6,6],
    [2,2,2,2,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2,2,3,3,2,2,1,1,1,1,2,2,2,2,2,2,2,6,2,6,6,6,6,6,6],
    [2,3,3,2,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,3,3,2,1,1,2,2,2,2,2,2,2,6,2,6,6,6,6,6,6,6,6],
    [3,3,3,2,1,1,1,1,1,1,1,2,1,1,1,1,2,2,1,1,1,1,2,2,3,1,3,2,2,2,2,2,2,4,2,2,2,2,2,6,2,6,6,6,6,6,6,6],
    [3,4,5,2,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,1,1,2,1,2,2,2,2,4,4,2,2,2,2,6,2,2,6,6,6,6,6,6,6],
    [2,4,5,2,2,1,2,2,2,1,1,1,1,1,2,2,3,3,3,2,3,3,3,2,2,3,2,2,2,2,2,4,4,2,2,2,6,2,6,2,2,2,3,3,6,6,6,0],
    [2,4,2,2,2,2,2,2,2,2,2,1,1,2,2,1,1,3,3,3,1,1,3,3,1,2,2,2,2,2,2,2,2,2,2,2,2,6,2,2,3,3,3,6,6,6,6,0],
    [0,2,2,2,2,2,2,2,2,2,2,2,1,2,2,1,2,2,3,1,1,2,2,3,3,2,2,2,2,2,2,2,2,2,2,2,6,2,2,5,5,3,5,6,6,6,6,0],
    [0,2,2,2,2,2,2,2,2,2,2,2,1,2,2,2,2,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,6,2,6,2,6,5,5,5,6,6,6,6,6,0],
    [0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,2,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,6,2,6,2,6,5,5,5,5,6,6,6,6,0,0],
    [0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,2,2,2,6,2,6,2,6,5,5,5,5,6,6,6,6,6,0,0],
    [0,0,0,2,6,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,6,2,6,2,2,3,6,6,5,5,6,6,6,6,6,0,0,0],
    [0,0,0,6,2,6,2,6,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,6,2,6,2,6,6,2,6,5,5,6,6,6,6,6,6,0,0,0],
    [0,0,0,0,6,2,6,2,6,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,6,2,6,2,6,2,6,6,2,3,3,5,5,6,6,6,6,6,0,0,0,0],
    [0,0,0,0,0,6,6,2,6,2,6,2,2,2,2,2,2,2,2,2,2,2,2,2,6,2,6,2,6,2,6,6,6,6,6,2,2,5,6,6,6,6,6,0,0,0,0,0],
    [0,0,0,0,0,0,6,6,2,6,2,6,2,6,2,6,2,6,2,6,2,6,2,6,2,6,2,6,2,6,6,6,6,6,6,6,6,6,6,6,6,6,0,0,0,0,0,0],
    [0,0,0,0,0,0,6,6,6,6,6,2,6,2,6,2,6,2,6,2,6,2,6,2,6,2,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,6,6,6,6,6,6,6,6,6,2,6,2,6,2,6,2,6,2,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,6,6,6,6,6,6,6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

world3colors = [None, (115, 23, 44), (59, 23, 37), (223, 63, 35), (250, 106, 10), (36, 34, 52), (249, 164, 27)]
world3 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,1,2,2,2,1,1,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,2,3,1,1,2,2,1,1,1,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,2,1,3,1,1,1,1,2,1,1,1,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,4,1,1,1,1,1,1,1,1,2,1,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,2,1,1,4,1,1,1,2,2,2,2,1,1,2,2,2,2,2,4,4,3,3,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,4,2,2,2,2,1,2,2,1,2,2,1,4,4,4,2,2,2,2,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,1,1,2,2,1,1,1,1,1,1,4,2,2,1,1,4,4,4,4,4,4,3,3,4,2,2,2,2,2,2,5,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,2,2,4,2,4,4,4,4,3,3,1,4,4,4,3,2,2,2,2,2,2,2,2,5,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,1,1,1,2,1,1,1,1,1,2,1,1,3,4,4,1,6,4,2,1,1,1,1,1,4,4,2,2,2,2,2,2,2,2,0,0,0,0,0,0],
    [0,0,0,0,0,1,1,1,1,2,1,1,1,2,2,1,1,1,1,1,4,3,1,6,4,1,2,2,1,1,1,1,1,4,2,2,2,2,2,2,2,2,5,0,0,0,0,0],
    [0,0,0,0,1,1,1,2,1,1,1,1,2,2,1,1,1,1,1,1,4,3,3,4,4,1,2,2,1,1,1,1,1,1,4,2,2,2,2,2,2,2,5,5,0,0,0,0],
    [0,0,0,2,2,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,4,1,4,4,1,1,2,2,1,1,1,1,1,1,2,4,2,2,2,2,2,2,5,5,5,0,0,0],
    [0,0,0,1,1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,3,4,4,1,1,2,2,1,1,1,2,1,1,2,2,3,2,2,2,2,2,2,2,5,5,0,0,0],
    [0,0,1,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,4,1,1,1,1,2,2,2,1,1,1,1,1,1,2,2,2,3,2,2,2,2,2,5,5,5,5,0,0],
    [0,0,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,4,4,1,1,2,2,2,2,1,1,1,1,1,1,1,2,2,1,1,3,2,2,2,2,5,2,5,5,0,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,4,1,1,2,1,1,1,1,1,1,1,1,1,1,1,2,2,2,4,6,2,2,2,2,2,5,5,5,5,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,4,4,2,2,2,2,5,2,5,5,5,0],
    [0,1,1,1,1,1,1,1,1,1,3,4,4,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,4,4,2,2,2,5,2,5,5,5,0],
    [0,3,1,1,1,1,4,1,4,4,3,1,1,1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,4,2,2,2,2,5,5,5,5,0],
    [1,1,1,3,4,4,4,4,1,1,1,1,1,2,1,1,1,2,1,1,1,1,1,2,2,1,1,1,1,1,1,2,2,1,2,1,2,2,3,1,4,4,5,2,5,5,5,5],
    [1,1,1,1,1,1,1,3,4,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,1,3,2,2,3,3,4,4,5,5],
    [1,1,1,2,1,1,1,1,1,4,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,2,2,1,2,2,2,2,4,4,2,2,2,2,5,5,5,3,5],
    [1,1,1,1,1,2,2,1,1,1,4,1,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,2,1,1,2,2,2,2,2,4,4,2,2,2,5,5,5,5,5,3],
    [1,2,1,1,1,1,1,2,2,1,1,4,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,4,4,3,4,2,2,5,2,5,5,5,5],
    [2,2,2,1,1,1,1,1,1,1,1,4,3,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,2,2,2,1,2,4,4,3,1,3,2,5,2,5,5,5,5,5],
    [2,2,1,2,1,1,1,1,1,1,4,3,3,2,1,2,1,1,2,2,1,1,1,1,1,2,2,3,1,1,2,1,2,2,2,4,4,2,3,2,2,5,2,5,5,5,5,5],
    [2,2,2,2,1,1,1,1,1,1,3,4,1,1,2,2,2,2,2,1,1,1,1,1,1,1,2,1,3,2,2,2,2,4,4,3,4,2,2,2,5,2,5,5,5,5,5,5],
    [2,2,2,1,2,1,1,1,1,4,4,1,1,1,1,2,2,2,2,1,1,1,1,1,1,1,1,1,2,3,4,4,4,4,2,2,6,2,2,5,2,5,5,5,5,5,5,5],
    [2,2,2,2,2,2,1,1,4,4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,4,4,3,4,2,4,6,4,2,2,5,2,5,5,5,5,5,5,5],
    [0,2,2,2,2,1,2,4,1,1,4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,3,1,4,2,2,2,4,4,3,5,2,5,2,5,5,5,5,5,0],
    [0,2,2,2,2,2,4,1,1,1,1,1,4,3,4,1,1,1,1,1,1,1,1,1,1,1,1,2,4,1,3,4,2,2,2,2,4,3,2,5,2,5,5,5,5,5,5,0],
    [0,2,2,2,2,2,4,2,1,1,1,1,1,4,1,4,4,3,3,4,1,1,1,1,1,2,2,4,4,3,4,2,2,2,2,2,2,4,4,4,4,5,5,5,5,5,5,0],
    [0,2,2,2,2,2,2,2,2,1,1,1,4,1,1,1,1,1,4,4,4,1,1,2,2,2,4,4,3,3,4,2,2,2,2,2,5,2,5,2,4,4,5,5,5,5,5,0],
    [0,0,2,2,2,2,2,2,2,1,1,4,2,2,2,2,2,1,4,1,4,1,1,1,2,4,3,3,3,6,4,4,2,2,2,5,2,5,2,5,5,5,4,5,5,5,0,0],
    [0,0,2,5,2,2,2,2,2,2,4,4,2,2,2,2,2,4,4,4,1,4,4,4,4,4,3,3,3,6,4,4,2,2,2,5,2,5,5,5,5,5,5,5,5,5,0,0],
    [0,0,0,2,5,2,2,2,2,4,1,3,4,2,1,1,4,2,2,4,3,4,4,3,3,3,3,6,1,3,3,4,2,2,5,2,5,5,5,5,5,5,5,3,5,0,0,0],
    [0,0,0,5,2,5,2,2,4,4,3,1,3,3,4,4,2,2,2,2,4,3,3,4,4,3,3,3,6,1,1,3,4,5,2,5,5,5,5,5,5,5,5,3,5,0,0,0],
    [0,0,0,0,5,5,2,5,2,4,4,4,4,2,2,2,3,2,2,3,2,2,2,4,4,4,4,4,4,3,3,3,4,4,2,5,5,5,5,5,5,5,5,5,0,0,0,0],
    [0,0,0,0,0,5,5,2,5,2,4,2,2,2,2,2,2,3,3,2,2,2,2,2,4,4,4,4,4,4,3,4,3,4,4,5,5,5,5,5,5,5,5,0,0,0,0,0],
    [0,0,0,0,0,0,5,5,2,5,4,5,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,5,2,5,4,4,4,4,5,5,5,5,5,5,5,0,0,0,0,0,0],
    [0,0,0,0,0,0,5,5,5,3,2,5,2,5,2,5,2,5,2,5,2,5,2,5,2,5,2,5,2,5,5,2,5,4,4,5,5,5,5,5,5,5,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,5,5,3,5,5,5,2,5,2,5,2,5,2,5,2,5,2,5,2,5,2,5,5,5,5,5,5,4,5,5,5,5,5,5,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,5,5,5,5,5,5,5,2,5,2,5,2,5,2,5,2,5,5,5,5,5,5,5,5,5,5,4,5,5,5,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,3,5,5,5,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,3,5,5,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,5,5,5,5,5,5,5,5,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]

world4colors = [None, (139, 147, 175), (74, 84, 98), (71, 125, 133)]
world4 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,2,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,1,1,1,2,2,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,2,2,2,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,2,2,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,2,3,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,1,1,1,1,1,1,1,1,1,1,2,1,2,2,2,3,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,3,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,3,3,0,0,0,0,0,0],
    [0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,3,1,1,1,1,1,1,1,1,1,1,1,2,1,2,2,2,3,3,3,0,0,0,0,0],
    [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,3,2,3,3,3,0,0,0,0],
    [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,3,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,3,2,3,3,0,0,0,0],
    [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,3,2,3,3,3,0,0,0],
    [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,3,3,3,3,0,0],
    [0,0,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,3,2,3,3,3,3,0,0],
    [0,0,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,0,0],
    [0,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,3,1,1,1,1,1,1,1,1,1,1,2,2,2,2,3,2,3,3,3,3,0],
    [0,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,3,1,1,1,1,1,1,1,1,1,1,2,1,2,2,2,2,3,3,3,3,3,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3],
    [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,3,2,2,3,3,3,3,3,3],
    [2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,3,2,3,2,3,3,3,3,3],
    [2,2,1,1,1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,2,1,2,2,3,2,2,2,3,3,3,3,3,3],
    [2,3,1,1,1,1,1,2,2,2,2,1,1,1,1,1,1,1,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,2,1,2,2,2,2,2,2,2,3,3,3,3,3,3],
    [3,1,1,1,1,1,1,2,2,2,3,1,1,1,1,1,1,1,2,2,2,2,2,2,2,1,1,1,1,1,1,2,1,2,1,2,2,2,2,2,2,3,3,3,3,3,3,3],
    [1,1,1,1,1,1,1,2,2,2,1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,1,1,1,1,1,2,1,1,1,2,2,2,2,2,2,3,2,3,3,3,3,3,3],
    [1,1,1,1,1,1,2,2,2,3,1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,1,1,1,1,1,1,2,1,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3],
    [1,1,1,1,1,1,1,2,3,1,1,1,1,1,1,1,1,1,2,2,2,2,2,3,1,1,1,1,1,2,1,2,1,2,2,2,2,2,2,3,2,3,3,3,3,3,3,3],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,3,3,3,3,1,1,2,1,2,1,2,1,2,2,2,2,2,2,3,2,3,3,3,3,3,3,3,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,2,2,2,2,2,2,3,2,3,3,3,3,3,3,3,0],
    [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,2,2,2,2,2,3,2,3,2,3,3,3,3,3,3,3,3,0],
    [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,2,2,2,2,2,3,2,3,2,3,3,3,3,3,3,3,3,0,0],
    [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,2,2,2,1,2,2,2,2,2,2,2,2,3,2,3,3,3,3,3,3,3,3,0,0],
    [0,0,1,2,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,2,1,2,1,2,2,2,2,2,2,2,2,2,2,3,2,3,2,3,3,3,3,3,3,3,3,3,0,0],
    [0,0,0,1,1,1,2,1,2,2,1,1,1,1,2,1,2,1,2,1,2,1,2,2,2,2,2,2,2,2,2,2,3,2,3,2,3,3,3,3,3,3,3,3,3,0,0,0],
    [0,0,0,0,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,2,2,2,2,2,2,3,2,3,2,3,2,3,3,3,3,3,3,3,3,3,3,0,0,0,0],
    [0,0,0,0,2,2,2,2,2,2,1,2,1,2,1,2,1,2,2,2,2,2,2,2,2,2,2,3,2,3,2,3,2,2,3,3,3,3,3,3,3,3,3,3,0,0,0,0],
    [0,0,0,0,0,2,2,2,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,2,3,2,2,2,3,2,3,2,2,3,3,3,3,3,3,3,3,3,3,0,0,0,0,0],
    [0,0,0,0,0,0,3,2,2,2,2,2,2,2,3,2,2,2,2,2,2,2,2,2,3,2,3,2,3,2,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,3,2,3,2,2,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,2,3,3,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,2,3,2,3,2,3,2,3,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

world5colors = [None, (34, 80, 56), (90, 78, 66), (33, 170, 242), (50, 132, 100), (39, 93, 202), (50, 112, 79), (91, 174, 139), (51, 58, 64), (30, 217, 203), (234, 229, 252), (88, 141, 190), (72, 125, 133)]
world5 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,2,1,1,1,1,3,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,4,4,4,4,1,1,1,3,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,1,1,1,5,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,4,3,4,4,4,4,4,4,4,6,4,6,4,4,4,6,6,6,4,4,3,5,5,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,4,4,3,4,4,4,7,4,4,4,6,6,6,6,4,4,4,7,6,4,4,4,3,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,4,4,4,4,3,4,4,7,4,4,4,7,6,6,6,7,4,4,6,6,4,4,4,3,1,1,4,1,1,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,4,4,4,7,4,4,3,4,4,4,4,7,7,4,4,6,7,4,7,4,4,4,4,4,3,3,4,4,1,1,1,1,8,8,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,4,4,7,7,4,4,3,4,4,4,4,4,4,4,4,4,7,7,7,7,7,4,4,4,4,3,4,4,4,1,4,1,1,1,8,8,0,0,0,0,0,0],
    [0,0,0,0,0,0,4,4,4,4,4,3,4,4,4,4,4,4,4,4,4,9,7,7,7,7,4,4,4,4,3,3,4,4,4,4,1,1,1,1,1,8,0,0,0,0,0,0],
    [0,0,0,0,0,4,4,3,3,3,3,3,4,4,4,4,4,4,4,4,9,7,7,4,7,7,4,4,4,9,9,9,4,4,4,4,4,1,1,1,8,8,8,0,0,0,0,0],
    [0,0,0,0,4,4,3,3,4,3,3,4,4,7,7,4,7,7,7,7,a,1,1,1,9,1,1,1,9,9,3,4,4,4,4,4,1,1,1,1,1,8,8,9,0,0,0,0],
    [0,0,0,4,4,4,4,4,4,3,4,4,4,2,7,7,7,7,7,a,4,4,9,9,1,1,1,9,a,a,a,9,4,4,4,4,4,1,1,1,8,1,8,9,b,0,0,0],
    [0,0,0,4,4,4,7,4,3,4,4,4,4,4,2,7,7,7,a,7,7,a,a,9,4,9,a,a,a,a,a,a,9,7,4,4,1,1,1,1,8,1,9,b,b,0,0,0],
    [0,0,a,9,4,4,7,3,4,4,4,4,4,7,7,7,7,7,a,a,a,a,a,a,a,a,a,a,a,a,a,9,7,7,7,4,1,4,1,1,1,b,b,b,b,b,0,0],
    [0,0,a,a,9,9,7,3,4,4,4,7,7,7,2,7,7,7,9,a,a,a,a,a,a,a,a,9,9,9,a,9,7,7,7,7,4,1,1,1,8,1,8,c,b,b,0,0],
    [0,a,a,a,a,3,7,3,4,4,7,7,7,2,2,7,7,7,7,9,a,a,a,a,a,a,9,4,4,4,7,7,7,7,7,7,4,4,1,1,8,1,b,b,b,b,c,0],
    [0,a,a,a,a,9,9,3,9,7,7,7,2,7,7,7,7,a,7,4,9,9,a,a,a,a,9,9,9,4,7,7,7,7,7,7,7,1,1,1,1,9,9,b,b,b,c,0],
    [0,a,a,a,a,a,a,a,a,a,9,2,7,7,7,7,7,9,7,3,3,4,4,9,9,a,a,9,4,4,4,4,7,7,7,7,7,4,1,1,9,b,b,b,b,c,c,0],
    [0,a,a,a,a,a,a,a,a,a,9,2,2,7,7,7,7,7,a,9,4,4,4,4,4,4,3,4,4,4,4,4,4,4,2,7,7,1,4,1,b,b,b,c,c,c,c,0],
    [4,a,a,a,a,a,a,9,a,a,2,2,7,7,7,7,7,4,4,3,a,a,4,4,4,4,4,4,4,4,4,7,7,7,2,7,7,4,9,9,b,b,b,b,b,c,c,8],
    [1,4,9,a,a,a,a,a,9,7,7,7,7,7,7,7,7,7,4,3,4,4,4,4,4,4,4,4,4,4,4,7,7,7,2,7,7,4,9,9,9,b,b,b,b,8,8,8],
    [1,4,4,9,9,9,9,9,9,7,7,7,7,7,7,7,7,7,7,7,4,4,4,4,4,4,4,4,4,4,4,7,7,2,2,7,4,2,b,b,b,b,8,8,8,8,8,8],
    [1,1,4,4,4,7,9,7,7,7,7,7,7,7,7,7,7,4,4,4,4,4,4,4,4,4,4,4,4,7,7,2,2,2,2,7,2,2,9,b,b,8,1,8,8,8,8,8],
    [1,1,1,4,4,7,7,4,7,7,7,7,1,1,7,7,7,4,4,4,4,4,4,4,4,4,4,4,7,2,7,7,7,2,7,4,2,2,1,9,b,b,1,8,8,8,8,8],
    [1,1,1,4,4,4,7,4,4,7,7,1,1,1,1,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,7,2,2,1,4,4,1,1,1,8,1,8,8,8,8,8,8],
    [3,3,1,1,4,3,4,7,4,4,4,1,1,1,1,1,4,4,4,4,a,a,a,4,4,9,4,4,4,4,4,7,2,1,4,4,1,1,1,8,1,8,8,8,8,8,8,8],
    [1,1,3,3,3,4,4,7,7,4,4,4,1,7,7,7,4,4,7,a,a,a,a,a,a,9,9,4,4,4,4,4,4,4,4,1,1,1,8,1,8,1,8,8,8,8,8,8],
    [1,1,3,1,1,4,4,4,7,7,4,2,7,7,7,2,7,7,7,a,a,a,a,a,b,b,4,4,3,3,5,4,4,4,1,1,1,1,8,1,8,8,8,8,8,8,8,8],
    [1,1,1,5,1,4,4,4,4,4,4,2,2,2,7,2,7,7,7,9,a,a,b,b,b,4,4,3,3,3,5,5,4,4,1,1,1,8,1,8,1,8,8,8,8,8,8,8],
    [0,1,1,1,5,1,4,4,4,4,4,4,2,2,2,2,2,2,2,4,a,b,4,4,4,4,3,3,3,5,5,4,4,4,1,1,8,1,8,1,1,8,8,8,8,8,8,0],
    [0,1,1,1,1,1,4,4,4,4,4,4,4,4,2,2,7,7,4,4,4,4,4,4,4,4,4,3,5,5,4,4,4,4,1,1,8,1,8,1,8,8,c,8,8,8,8,0],
    [0,1,1,1,1,4,4,4,4,4,4,7,7,7,7,4,4,4,4,4,4,4,4,3,4,4,4,4,4,4,4,4,4,1,1,8,1,8,1,8,8,c,c,8,8,8,8,0],
    [0,1,1,1,1,1,4,4,4,7,7,4,7,7,4,4,4,4,4,4,4,4,4,3,4,4,4,4,4,4,4,4,4,1,8,1,8,a,1,8,c,c,c,c,8,8,8,0],
    [0,0,1,1,1,4,1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,4,4,4,4,4,4,4,1,1,8,1,a,1,8,a,c,c,c,8,8,8,0,0],
    [0,0,1,1,1,1,1,1,4,1,4,1,1,4,4,4,4,4,4,4,4,4,4,4,3,4,1,4,1,4,1,1,1,8,1,a,a,8,a,a,c,c,8,8,8,8,0,0],
    [0,0,0,1,1,1,1,1,1,1,1,1,4,1,4,4,4,4,4,4,4,4,4,4,3,4,1,1,1,1,1,1,8,1,8,a,c,a,a,c,c,c,c,8,8,0,0,0],
    [0,0,0,1,1,1,1,1,1,1,1,1,1,1,a,a,4,a,a,a,4,4,a,4,1,9,1,1,1,1,8,1,8,a,a,c,c,c,c,c,c,8,8,8,8,0,0,0],
    [0,0,0,0,1,1,1,1,1,1,1,1,1,a,a,a,a,a,a,4,4,a,a,1,1,1,5,8,1,8,1,8,1,8,c,c,c,c,c,8,8,8,8,8,0,0,0,0],
    [0,0,0,0,0,8,1,1,1,1,1,a,a,a,a,a,a,a,c,1,1,1,1,1,1,5,8,5,8,1,8,1,1,c,c,c,c,c,8,c,c,8,8,0,0,0,0,0],
    [0,0,0,0,0,0,8,1,8,1,8,a,a,a,c,a,c,1,1,1,8,1,8,1,8,5,8,5,5,8,1,8,8,8,c,c,c,c,c,c,8,8,0,0,0,0,0,0],
    [0,0,0,0,0,0,8,8,1,8,1,8,c,c,c,c,1,8,1,8,1,8,1,8,1,8,1,8,5,5,5,8,c,c,c,c,c,c,c,8,8,8,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,8,8,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,1,8,5,8,8,c,c,c,c,c,8,c,8,8,8,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,8,8,8,8,8,8,1,8,1,8,1,8,1,8,1,8,8,8,8,8,5,8,8,c,c,c,8,8,8,8,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,8,8,8,8,8,8,8,8,8,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

world6colors = [None, (47, 135, 36), (38, 77, 47), (33, 170, 242), (54, 60, 70), (39, 93, 202), (234, 255, 252), (125, 174, 59), (90, 78, 66), (163, 183, 134), (93, 142, 173)]
world6 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,2,2,3,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,2,3,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3,3,3,2,2,2,5,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,5,5,2,2,2,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,6,6,1,1,1,1,7,1,1,1,1,1,1,1,1,1,7,1,1,1,1,1,3,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,6,6,6,6,1,1,1,7,1,1,1,7,1,1,1,7,1,1,1,1,6,6,1,3,2,2,1,2,2,2,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,6,6,6,6,6,6,1,1,1,1,9,7,1,1,1,7,1,7,6,6,7,1,1,3,3,1,1,2,2,2,2,2,4,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,9,6,6,6,9,1,9,6,6,1,9,1,1,1,1,7,7,7,7,7,7,7,1,1,3,1,1,1,2,1,2,2,2,2,4,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,9,6,6,6,9,1,1,9,6,1,1,1,1,7,7,7,7,7,1,1,1,1,3,3,1,1,1,1,2,2,2,2,2,2,0,0,0,0,0,0],
    [0,0,0,0,0,1,1,1,9,9,9,1,9,9,1,1,1,1,1,1,1,7,7,1,7,7,1,1,1,1,3,3,1,1,1,1,1,2,2,2,2,2,4,0,0,0,0,0],
    [0,0,0,0,1,1,1,1,1,9,6,1,1,7,7,1,7,7,7,7,7,1,1,1,1,1,1,1,1,3,3,1,1,1,1,1,2,2,2,2,2,2,2,4,0,0,0,0],
    [0,0,0,1,1,1,1,1,1,1,9,6,1,8,6,7,7,7,7,7,7,7,1,1,1,1,1,3,3,3,1,1,1,1,1,1,1,2,2,2,2,2,2,4,4,0,0,0],
    [0,0,0,1,1,1,7,1,1,1,1,9,9,6,8,7,7,7,7,7,7,7,1,1,1,3,3,1,1,1,1,7,7,7,1,1,2,2,2,2,2,2,4,4,4,0,0,0],
    [0,0,1,1,1,1,7,1,1,1,1,1,1,7,7,7,7,7,7,7,7,1,1,3,3,3,1,1,1,1,1,7,7,7,7,1,9,9,2,2,2,2,4,4,4,4,0,0],
    [0,0,1,1,1,7,7,1,1,1,1,7,7,7,8,7,7,7,7,7,1,1,3,1,1,1,1,1,1,6,6,7,7,7,6,9,1,2,2,2,2,2,4,4,4,4,0,0],
    [0,1,1,1,1,1,7,1,1,1,7,7,7,8,8,7,7,7,7,1,1,3,1,1,1,1,1,9,6,6,6,6,6,6,7,7,1,1,2,2,2,4,2,4,4,4,4,0],
    [0,1,1,1,1,1,1,1,1,7,7,7,8,7,7,7,7,7,7,1,3,1,1,1,1,1,6,6,6,6,6,6,6,7,7,7,7,2,2,a,a,2,4,4,4,4,4,0],
    [0,1,1,1,7,7,7,7,7,7,7,8,7,7,7,7,7,7,7,3,3,1,1,1,1,1,6,6,6,6,6,6,6,9,9,9,9,2,a,2,2,2,4,4,4,4,4,0],
    [0,1,1,7,7,7,7,8,8,7,8,8,8,7,7,7,7,7,1,3,1,1,1,1,1,1,9,6,9,6,6,9,9,9,9,7,7,2,1,2,2,4,2,4,4,4,4,0],
    [1,1,1,1,7,7,7,7,7,8,8,8,7,7,7,7,7,1,1,3,1,1,1,1,1,1,1,9,9,9,9,9,9,9,8,7,7,1,2,2,2,2,4,4,4,4,4,4],
    [2,1,1,1,7,7,7,7,7,7,7,7,7,7,7,7,7,7,1,3,1,1,1,1,1,1,1,1,9,9,9,9,9,9,8,7,7,1,2,2,2,2,4,4,a,a,a,a],
    [2,2,1,1,1,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,1,1,1,1,1,1,1,1,1,9,9,7,7,8,8,7,1,1,2,2,2,4,2,4,a,a,a,a],
    [2,2,2,1,1,7,7,7,7,7,7,7,7,7,7,7,7,1,1,1,1,1,1,1,1,1,1,1,1,7,9,9,8,8,8,7,8,8,2,2,4,2,4,a,a,a,a,a],
    [2,2,2,1,1,7,7,7,7,7,7,1,1,7,7,7,1,1,1,1,1,1,1,1,1,1,1,1,7,2,7,7,7,8,7,1,8,8,2,2,4,2,4,a,a,a,a,a],
    [2,2,2,1,1,1,7,7,7,7,7,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,7,8,8,2,1,1,2,2,4,2,4,a,a,a,a,a,a],
    [3,3,2,2,1,3,1,7,7,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,7,2,2,1,1,2,2,2,2,a,a,a,a,a,a,a,a],
    [2,2,3,3,3,1,1,7,7,1,1,1,7,7,7,1,1,7,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,4,2,a,a,a,a,a,a,a,a],
    [2,2,3,2,2,1,1,1,7,7,8,7,7,7,8,7,7,7,8,1,1,1,1,1,1,1,1,1,3,3,5,1,1,1,2,2,2,2,2,4,2,a,a,a,a,a,a,a],
    [2,2,2,5,2,1,1,1,1,1,1,8,8,7,8,7,7,7,8,1,1,1,1,1,1,1,1,3,3,3,5,1,1,1,2,2,2,2,4,2,4,a,a,a,a,a,a,a],
    [0,2,2,2,5,2,1,1,1,1,1,1,8,8,8,8,8,8,1,1,1,1,1,1,1,1,1,3,3,5,1,1,1,1,2,2,2,4,2,4,a,a,a,a,a,a,a,0],
    [0,2,2,2,2,2,1,1,1,1,1,1,1,8,8,9,7,1,1,1,1,1,1,9,9,1,1,1,1,1,1,1,1,1,2,2,a,a,a,a,a,a,a,a,a,a,4,0],
    [0,2,2,2,2,1,1,1,1,1,7,7,7,7,9,9,1,1,1,1,1,9,6,6,1,1,1,9,1,1,1,1,1,2,2,2,4,2,4,4,a,a,a,a,4,4,4,0],
    [0,2,2,2,2,2,1,9,7,7,6,7,7,9,9,1,1,1,1,1,9,6,6,6,6,6,6,6,1,1,1,1,1,2,4,2,4,2,a,a,a,a,4,4,4,4,4,0],
    [0,0,2,2,2,2,9,1,1,9,7,7,7,9,1,1,1,6,6,6,6,9,9,6,6,9,9,6,1,1,1,1,2,4,2,4,2,4,4,4,4,4,4,4,4,4,0,0],
    [0,0,2,2,2,2,a,1,9,2,2,2,2,9,6,6,6,6,9,9,9,9,9,9,9,9,9,9,9,2,2,2,4,2,4,2,4,4,4,4,4,4,4,4,4,4,0,0],
    [0,0,0,2,2,2,2,2,a,2,2,1,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,2,4,2,4,2,2,4,4,4,4,4,4,4,4,4,4,0,0,0],
    [0,0,0,4,2,4,2,4,a,2,2,2,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,2,4,2,4,2,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0],
    [0,0,0,0,4,2,4,2,4,a,2,2,9,9,9,9,9,a,a,9,a,a,9,a,a,9,4,a,a,a,4,2,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0],
    [0,0,0,0,0,4,4,2,4,2,4,2,2,a,a,9,a,a,2,2,2,a,a,a,4,2,4,2,4,2,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0],
    [0,0,0,0,0,0,4,4,2,4,2,4,2,4,a,a,2,4,2,4,2,4,2,4,2,4,5,5,2,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0],
    [0,0,0,0,0,0,4,4,4,4,4,2,4,2,4,a,a,2,4,2,4,2,4,2,4,2,4,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,4,4,4,4,4,4,4,4,4,2,4,2,4,2,4,2,4,2,4,4,5,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

world7colors = [None, (197, 128, 101), (139, 60, 50), (74, 19, 59), (92, 20, 31), (181, 101, 72), (120, 2, 64), (121, 75, 76), (75, 45, 69)]
world7 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,2,2,2,2,2,2,2,3,3,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,2,2,2,2,2,2,4,3,3,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,4,5,2,4,3,3,3,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,2,3,3,0,0,0,0,0,0,0,0,0,1,2,2,2,2,2,2,2,4,5,2,4,3,3,3,3,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,2,3,3,3,3,0,0,0,0,0,0,0,1,2,2,2,2,2,2,2,2,5,2,4,4,3,3,3,3,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,2,3,3,3,3,3,3,0,0,0,0,0,0,2,2,2,4,5,2,2,2,2,2,2,4,3,3,3,3,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,6,0,0,0,0,0,0,0,2,2,4,5,2,2,2,2,2,2,4,4,3,3,3,3,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,6,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,4,4,4,3,3,3,3,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,3,0,6,6,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,4,4,4,3,3,3,3,3,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,4,4,4,3,3,3,3,6,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,4,4,3,3,3,3,3,6,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,4,2,2,4,4,3,3,3,3,3,6,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,4,4,4,4,3,3,3,3,3,6,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,1,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,2,2,2,2,2,2,5,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,2,2,2,2,5,5,2,2,2,2,2,2,2,2,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,2,2,0,0,0,0,0,0,0],
    [0,0,0,0,2,2,2,2,2,2,2,2,2,4,2,2,2,4,4,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,2,2,0,0,0,0,0,0],
    [0,0,0,0,2,2,2,2,2,2,2,2,2,4,4,2,4,4,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,2,2,4,4,0,0,0,0,0],
    [0,0,0,0,0,2,2,2,2,2,2,2,2,2,4,4,4,4,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,1,1,2,2,2,2,2,2,4,3,3,0,0,0,0],
    [0,0,0,0,0,0,4,2,2,2,2,2,2,2,4,4,4,4,3,3,3,3,0,0,0,0,0,0,0,0,0,1,1,2,2,2,2,2,2,2,2,4,3,3,0,0,0,0],
    [0,0,0,0,0,0,4,4,4,2,2,2,2,2,4,4,4,4,3,3,3,6,0,0,0,0,0,0,0,0,1,2,2,2,2,2,2,2,2,2,4,3,3,3,0,0,0,0],
    [0,0,0,0,0,3,3,4,4,4,2,2,2,2,4,4,4,3,3,3,6,0,0,0,0,0,0,0,0,1,2,2,2,2,2,2,2,2,2,2,4,3,3,3,0,0,0,0],
    [0,0,0,0,0,3,3,3,4,4,4,2,2,4,4,4,4,3,3,3,6,0,0,0,0,0,0,0,1,2,2,2,2,2,2,2,2,2,2,4,3,3,3,3,0,0,0,0],
    [0,0,0,0,0,3,3,3,3,3,4,4,4,4,4,4,4,3,3,3,6,0,0,0,0,0,0,0,2,2,2,2,2,4,2,2,2,2,2,4,3,3,3,3,0,0,0,0],
    [0,0,0,0,0,3,3,3,3,3,3,3,3,4,4,4,3,3,3,3,6,0,0,0,0,0,0,0,2,2,2,2,4,4,5,2,2,4,4,3,3,3,3,3,0,0,0,0],
    [0,0,0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,6,6,0,0,0,0,0,0,0,2,2,2,2,5,5,2,2,2,4,3,3,3,3,3,3,0,0,0,0],
    [0,0,0,0,0,0,3,3,3,3,3,3,3,3,3,3,3,3,6,6,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,4,3,3,3,3,3,3,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,6,6,6,6,6,6,6,6,6,6,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,4,4,3,3,3,3,3,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,4,4,4,4,3,3,3,3,3,6,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,4,4,4,3,3,3,3,3,3,6,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,4,4,4,4,3,3,3,3,3,6,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,4,4,4,4,4,4,3,3,3,3,3,3,6,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,2,4,4,3,3,3,3,3,3,3,3,6,6,6,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,4,4,3,3,3,3,3,3,3,6,6,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,3,3,6,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]

worlds = [Bitmap(world7, world7colors, "Malleandor", 6), Bitmap(world6, world6colors, "Tempus", 5), Bitmap(world5, world5colors, "Tempestus", 4), Bitmap(world1, world1colors, "Arbor", 0), Bitmap(world2, world2colors, "Nixpeculus", 1), Bitmap(world3, world3colors, "Ardor", 2), Bitmap(world4, world4colors, "Nilheld", 3)]