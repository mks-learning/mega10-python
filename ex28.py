def foo(name):
    greeting = 'Hi %s' %name.capitalize()
    return greeting


deets = input('What\'s your name?')
print(foo(deets))


# user_input = input("Enter your name:")
# message = "Hello %s " % (user_input)
# print(message)
