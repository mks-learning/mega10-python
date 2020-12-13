import pandas as pd

# objective count the trees that are hit on the way down the hit. Each row of the hill is infinitely wide
# BUT it repeats itself so you can always determine if you are going to hit a tree or find a space
# The toboggan travels at a slope of 1 row down and three columns across. 
# 
# thoughs 1) get the specific row you will encounter. 2) get the index (tree or space) that you will 
# encounter. 3) find that element, evaluate if it's a tree, if so add to the count of trees.  
# This attempt was heavily influenced by this reddit thread:
# https://www.reddit.com/r/adventofcode/comments/k83el3/my_day_3_experience_i_admit_i_might_be_doing/
#  

#read in the mountain
mountain = pd.read_csv('D3-input.csv', header=None)
# read in the row
terrain = [list(row) for row in mountain.values]
# read in the index item you want, which in this case it the increasing number x but it will always
# repeat. So use the remainer (modulo) 
currentItem, rowwidth, x_index, y_counter, item, tree, rowitems = 0, 0, 0, 0, 0, 0, 0
# CONSTANTS
# how long is the mountain?
totalrows = len(mountain)
# how many whole times does the mountain repeat?
rowwidth = len(terrain[0][0])

while y_counter < totalrows:
    #collect the current row elements
    currentrow = str(terrain[y_counter][0])
    # this is the slope of the tobagan
    currentItem = currentrow[x_index%rowwidth]
    # how wide is the mountain? (the constant)
    if currentItem == '#':
        tree += 1
    # updates the index for the row element to be analyzed
    y_counter += 2
    x_index = x_index + 1

print(str(totalrows)+" and each row is "+str(rowwidth)+' wide and you would encounter ')
print(str(tree) + ' trees in your journey down the mountain. The slope of the run was ')
print('rise of 2 and run of 1. The product of it all is '+str(84*198*72*81*53))

