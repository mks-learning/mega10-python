import csv

# reads in the input file and then converts it to integer value.
with open('Day1-stars_input.csv', 'r') as listObj:
    readin = csv.reader(listObj)
    rows = [int(row[0]) for row in readin]

# debug print command to make sure the content was read.
# print(rows)

i, j, k, answer = 0, 0, 0, 2020
while i < len(rows):
    while j < len(rows):
        while k < len(rows):
            if rows[i]+rows[j]+rows[k] == answer:
                print(rows[i]+rows[j]+rows[k])
                multanswer = rows[i]*rows[j]*rows[k]
                print(str(multanswer)+' is the value for the list items ' + str(rows[i])+" "+str(rows[j])+" "+str(rows[k]))
                quit()
            k += 1
        k=0
        j += 1
    j = 0
    i += 1

