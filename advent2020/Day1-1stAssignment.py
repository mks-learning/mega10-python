import csv

# reads in the input file and then converts it to integer value.
with open('stars_input.csv', 'r') as listObj:
    readin = csv.reader(listObj)
    rows = [int(row[0]) for row in readin]

# debug print command to make sure the content was read.
# print(rows)

i, j, answer = 0, 0, 2020
while i < len(rows):
    while j < len(rows):
        if rows[i]+rows[j] == answer:
            print(rows[i]+rows[j])
            multanswer = rows[i]*rows[j]
            print(str(multanswer)+' is the value for the list items '+str(rows[i])+" "+str(rows[j]))
            quit()
        j += 1
    j = 0
    i += 1

