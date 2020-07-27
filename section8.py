# objective is to create a program that allows the User to enter a phrase.
# If the phrase is not /end it continues if it continues it adds the phrase as
#  an element in a list data structure. Once the /end is encountered. the while
# loop is broken and the entire contents of the list is printed out in
# capitalize format.
#
# Always start with the output and work backwards or you will cause yourself
# unneeded stres
#

def sentence_maker(phrase):
    questioners = ('How', 'Who', 'What', 'When', 'Why', 'Where')
    capitalized = phrase.capitalize()
    if capitalized.startswith((questioners)):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)


something = []

while True:
    qq = input("Say something: ")
    if qq == '/end':
        break
    else:
        something.append(sentence_maker(qq))

print(' '.join(something))
