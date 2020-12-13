import pandas as pd

# read in the content of the CSV with a space delimit and then convert it to a list and 
# then split the list into more lists by index. so [A1, B1, C1] [A2, B2, C2], etc becomes
# [A1, A2, A3] and then [B1, B2, B3] etc.
# THERE ARE TWO TESTS...test one is the the validity of the counts of the test string
# The second test is the position of the test string in the password. Commented text
# in the body of the code is the first test

mountain = pd.read_csv('D3-input.csv')
terrain = [list(row) for row in mountain.values]
currentItem, rowwidth, repeated, x, y, item, space, tree = "", 0, 0, 0, 0, 0, 0, 0
newrow, currentrow, extrabits = [], [], []
# CONSTANTS
# how long is the mountain?
totalrows = len(mountain)
# how wide is the mountain?
rowwidth = int([len(i) for i in terrain[y]][0])
# how many whole times does the mountain repeat?
repeated = int(totalrows / rowwidth)
# how much extra needs to be added
extra_bit = totalrows % rowwidth

def extendRow(currentrow):
# This function takes the constants and specific row elements and makes it as wide as it is long
    counter, temprow, tempbits = 0, [], []
    temprow = currentrow[0]
    extrabits = [list(row) for row in currentrow[0]]
    tempbits = etrabits[0:extra_bit]
    # trying to make the extrabits froma list of lists to a single string
    while counter != extra_bit:
        tempbits = tempbits + str(extrabits[counter])
        countr +=1
    counter = 0
    while counter != repeated:
        temprow = temprow + str(currentrow[0])
        counter +=1
    temprow = temprow + str(tempbits[0:extra_bit])
    return temprow
 

while y < totalrows:
    currentrow = terrain[y]
    newrow = extendRow(currentrow)
    currentItem = str(newrow[x])
    while x < totalrows:
        if currentrow[x] == '.':
            space += 1
        else:
            tree += 1
    x = x + 3
    y += 1



print(str(rowtotal)+" and each row is this wide -> "+str(width))


'...##.....##..#..#....#.##.##.#...##.....##..#..#....#.##.##.#...##.....##..#..#....#.##.##.#...##.....##..#..#....#.##.##.#...##.....##..#..#....#.##.##.#...##.....##..#..#....#.##.##.#...##.....##..#..#....#.##.##.#...##.....##..#..#....#.##.##.#...##.....##..#..#....#.##.##.#...##.....##..#..#....#.##.##.#...##.....##..#..#....#.##.##.#...##.....##'