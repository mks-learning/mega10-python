import pandas as pd

# read in the content of the CSV with a space delimit and then convert it to a list and 
# then split the list into more lists by index. so [A1, B1, C1] [A2, B2, C2], etc becomes
# [A1, A2, A3] and then [B1, B2, B3] etc.

foo = pd.read_csv('Day2-input.csv', delim_whitespace=True)
bar = [list(row) for row in foo.values]


i=0
while i < len(bar):
    pwdLow, pwdHi = map(list, zip(*[s.split('-') for s in bar]))
    print(bar[i], pwdLow[i], pwdHi[i])
    i += 1















# bar = [list(row) for row in foo.values]
# ruleLow = [row[0] for row in bar]
# ruleHigh = [row[0] for row in bar]
# key = [row[1] for row in bar]
# test = [row[2] for row in bar]



# print(ruleLow)
# print(ruleHigh)
# print(key)
# print(test)


