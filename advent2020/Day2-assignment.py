import pandas as pd

# read in the content of the CSV with a space delimit and then convert it to a list and 
# then split the list into more lists by index. so [A1, B1, C1] [A2, B2, C2], etc becomes
# [A1, A2, A3] and then [B1, B2, B3] etc.
# THERE ARE TWO TESTS...test one is the the validity of the counts of the test string
# The second test is the position of the test string in the password. Commented text
# in the body of the code is the first test

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
    # str_test = tempassword.count(str(temptest[0]))
    low_test = tempassword[int(low)-1]
    high_test = tempassword[int(high)-1]
    test_low = (temptest[0] == low_test)
    test_high = ((temptest[0] == high_test))
 
    # test for first part of Day two assignment
    # # if (int(low) <= int(str_test) <= int(high)):
    #     i += 1
    # #rowNum += 1

    if ((test_low) and (test_high == False)):
        trueCount += 1
    elif ((test_low == False) and (test_high)):
        trueCount += 1
    rowNum += 1
print("The final answer to question 2 is "+str(trueCount)+".")