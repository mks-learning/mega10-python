import json
from difflib import get_close_matches

data = json.load(open('files/data.json'))


def getDef(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        answer = input('Did you mean %s ? (y/n)' %
            get_close_matches(w, data.keys())[0])
        if answer.lower() == 'y':
            return data[get_close_matches(w, data.keys())[0]]
        else:
            return "We didn\'t understand your entry. Try again."
    else:
        return "That word isn\'t in the dictionary. Try again."


query = input('What word would you like to look up?')
output = getDef(query)

if type(output) == list:
    print('The defintion for %s: ' % query)
    for item in output:
        print('- %s' % item)
else:
    print(output)
