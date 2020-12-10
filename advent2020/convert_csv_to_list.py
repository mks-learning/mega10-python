import csv
# import the csv library so you can read the csv file

# open file name (from the current location of the py file, else make the path relative)
# read the data into a temp variable that holds the contents of the file
# then list the items of that temp variable to store it into a LIST
# finally in a while loop print the contents with an iterator tied to the length of the list

with open('Day2-input.csv', 'r') as listObj:
    readData = csv.reader(listObj)
    pwdData = list(readData)

i = 0
while i < len(pwdData):
    print(pwdData[i])
    i += 1
    # i += 1 means increament i by one and it goes up from here through the loop 

import pandas as pd
# Create a dataframe from csv
df = pd.read_csv('students.csv', delimiter=',')
# User list comprehension to create a list of lists from Dataframe rows
list_of_rows = [list(row) for row in df.values]
# Print list of lists i.e. rows
print(list_of_rows)


# python code to demonstrate 
# splitting nested list 
# into 2 lists 
  
# initialising nested lists 
# ini_list = [[1, 2], [4, 3], [45, 65], [223, 2]] 
  
# # printing initial lists 
# print ("initial list", str(ini_list)) 
  
# # code to split it into 2 lists 
# res1 = [i[1] for i in ini_list] 
# res2 = [i[0] for i in ini_list] 
  
# # printing result 
# # print("final lists", str(res1), "\n", str(res2)) 
# import pandas as pd
# # Create a dataframe from csv
# df = pd.read_csv('students.csv', delimiter=',')
# # User list comprehension to create a list of lists from Dataframe rows
# list_of_rows = [list(row) for row in df.values]
# # Print list of lists i.e. rows
# print(list_of_rows)


