import mysql.connector
from difflib import get_close_matches


con = mysql.connector.connect(
user = "ardit700_student",
password = 'ardit700_student',
host = '108.167.140.122',
database = 'ardit700_pm1database'
)
# case1: 'item submitted gets a result'
# case2: 'Title case item gets a result'
# case3: 'Uppercase returns a result'
# case4: 'get a close match, confirm word, gets a result'
# case4n5: 'did not understand word'
# case5: 'no entry'


def getanswers(word):
    query_action: cursor.execute("SELECT * FROM Dictionary WHERE Expression = \
    '%s' " % word)
    results = cursor.fetchall()
    # debug line below
    print(results)
    return results


def getdef(word):
    results = ''
    if len(getanswers(word)) > 0:
        return results[word]
    elif len(getanswers(word.title(word))) > 0:
        return results[word]
    elif len(getanswers(word.upper(word))) > 0:
        return results[word]
    elif len(get_close_matches(word, results.keys()[0])) > 0:
        answer = input('Did you mean %s ? (y/n)' % results.keys()[0])
        if answer.lower() == 'y':
            return [get_close_matches(word, results.keys()[0])]
        else:
            return "Didn\'t understand your entry. Try again."
    else:
        return "Didn\'t find your entry. Try again."


# if w in data:
#     return data[w]
    # elif w.title() in data:
    #     # This is the case for a title word like Delhi
    #     return data[w.title()]
    # elif w.upper() in data:
    #     # This is the case for all caps entities
    #     return data[w.upper()]
    # elif len(get_close_matches(w, data.keys())) > 0:
    #     answer = input('Did you mean %s ? (y/n)' %
    #         get_close_matches(w, data.keys())[0])
    #     if answer.lower() == 'y':
    #         return data[get_close_matches(w, data.keys())[0]]
    #     else:
    #         return "We didn\'t understand your entry. Try again."
    # else:
    #     return "That word isn\'t in the dictionary. Try again."


cursor = con.cursor()
results = ''
word = input('What word would you like the definition? ')
answer = getdef(word)
# query = cursor.execute('SELECT * FROM Dictionary WHERE Expression = \'%s\''
#         % word)
# results = cursor.fetchall()


if results:
    for result in results:
        print(result[1])
else:
    print('No word found!')
