import pandas as pd

# read in the content of the CSV with a space delimit and then convert it to a list and 
# then split the list into more lists by index. so [A1, B1, C1] [A2, B2, C2], etc becomes
# [A1, A2, A3] and then [B1, B2, B3] etc.

foo = pd.read_csv('Day2-input.csv', delim_whitespace=True)
bar = [list(row) for row in foo.values]
rowNum, trueCount, i = 0, 0, 0
while rowNum < len(bar):
    # tempcount, tempchar, tempstring are the elements for this item of the list
    tempcount = bar[rowNum][0]
    temptest = bar[rowNum][1]
    tempassword = bar[rowNum][2]
    rule = tempcount.split('-')
    temptest = temptest.split(':')
    low = rule[0]
    high= rule[1]
    str_test = tempassword.count(str(temptest[0]))
    str_test_low = (temptest[0] == tempassword[int(low)-1])
    str_test_high = ((temptest[0] == tempassword[int(high)-1]))

    if (int(low) <= int(str_test) <= int(high)):
        i += 1
    #rowNum += 1

  
    if (int(low) <= int(str_test) <= int(high)) and str_test_low and str_test_high:
        trueCount += 1
    rowNum += 1
print("The final answer to the question 1 is "+str(i)+" and the final answer to question 2 is "+str(trueCount)+".")