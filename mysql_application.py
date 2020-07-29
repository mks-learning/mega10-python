import mysql.connector
from difflib import get_close_matches


con = mysql.connector.connect(
user="ardit700_student",
password="ardit700_student",
host="108.167.140.122",
database="ardit700_pm1database"
)
cursor = con.cursor()


def getanswers(word):
    cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
    results = cursor.fetchall()
    if len(results) > 0:
        return results[0]
    else:
        return 'Null'


def getdef(word):
    results = []
    if len(getanswers(word)) > 0 and getanswers(word) != 'Null':
        results = getanswers(word)
        return results
    elif len(getanswers(word.title())) > 0 and getanswers(word) != 'Null':
        results = getanswers(word)
        return results
    elif len(getanswers(word.upper())) > 0 and getanswers(word) != 'Null':
        results = getanswers(word)
        return results
    elif len(get_close_matches(word, getanswers(word))) > 0:
        answer = input('Did you mean %s ? (y/n)' % results)
        if answer == 'y':
            results = get_close_matches(word, getanswers(word))
            print('using get_close_matches, ' +
                  [get_close_matches(word, results)])
            return [get_close_matches(word, results)]
        else:
            return "Didn\'t understand your entry. Try again."
    else:
        return "Didn\'t find your entry. Try again."


word = 'Delhi'
print(getdef(word))

# cursor = con.cursor()
# results = ''
# word = input('What word would you like the definition? ')
# answer = getdef(word)
# # query = cursor.execute('SELECT * FROM Dictionary WHERE Expression = \'%s\''
# #         % word)
# # results = cursor.fetchall()
#
#
# if results:
#     for result in results:
#         print(result[1])
# else:
#     print('No word found!')
