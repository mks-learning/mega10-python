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
newrow, currentrow, temprow, extrabits = [], [], [], []
# CONSTANTS
# how long is the mountain?
totalrows = len(mountain)
# how wide is the mountain?
rowwidth = int([len(i) for i in terrain[y]][0])
# how many whole times does the mountain repeat?
repeated = int(totalrows / rowwidth)
# how much extra needs to be added
extra_bit = totalrows % rowwidth


def growRow(temprow, extrabits):
    counter = 0
    while counter != repeated:
        temprow = temprow + str(currentrow[0])
    counter +=1
    temprow = temprow + extrabits
    return temprow


while y < totalrows:
    currentrow = terrain[y]
    temprow = currentrow[0]
    extrabits = temprow[0:extra_bit]
    newrow = growRow(temprow, extrabits)
    currentItem = newrow[x]        
    if currentItem == '.':
        space += 1
        break
    else:
        tree += 1
        break    
    x = x + 3
    y += 1

print(str(totalrows)+" and each row is this wide -> "+str(rowwidth)+'. You would encounter ' +
       str(tree) + 'in your journey down the mountain.' )