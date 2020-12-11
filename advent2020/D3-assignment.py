import pandas as pd

# read in the content of the CSV with a space delimit and then convert it to a list and 
# then split the list into more lists by index. so [A1, B1, C1] [A2, B2, C2], etc becomes
# [A1, A2, A3] and then [B1, B2, B3] etc.
# THERE ARE TWO TESTS...test one is the the validity of the counts of the test string
# The second test is the position of the test string in the password. Commented text
# in the body of the code is the first test

foo = pd.read_csv('D3-input.csv')
bar = [list(row) for row in foo.values]
rowtotal = len(bar)
x, y, xloc, space, tree = 0, 0, "", 0, 0
while y < rowtotal:
    while x < rowtotal:
        rowcontent = bar[y]
        xloc = rowcontent[x]
        if xloc == '.':
            space += 1
        else:
            tree += 1
        x = x + 3
    y += 1



print(str(rowtotal)+" and each row is this wide -> "+str(width))