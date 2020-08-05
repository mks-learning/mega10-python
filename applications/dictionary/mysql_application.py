import mysql.connector
from difflib import get_close_matches


con = mysql.connector.connect(
user="ardit700_student",
password="ardit700_student",
host="108.167.140.122",
database="ardit700_pm1database"
)
word = input('What word would you like the definition? ')
cursor = con.cursor()
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
specific = cursor.fetchall()
# print(specific)
query_all = cursor.execute("SELECT * FROM Dictionary")
all = cursor.fetchall()
otherwords = get_close_matches(word, (val[0] for val in all))



def getdef(word):
    if len(specific) > 0:
        return specific
    elif len(get_close_matches(word, (val[0] for val in all))) > 0:
        answer = input('Did you mean %s ? (y/n) ' % otherwords[0])
        if answer == 'y':
            cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % otherwords[0])
            local = cursor.fetchall()
            return local
        else:
            nothing = "Didn\'t understand your entry. Try again."
            return nothing
    else:
        none = "Didn\'t find your entry. Try again."
        return none


answer = getdef(word)

if type(answer) == list:
    for result in answer:
        print(result[1])
else:
    print('No word found!')
