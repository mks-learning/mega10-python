# Define a function that takes an indefinite number of strings as parameters
# and returns a list containing all the strings in UPPERCASE and sorted
# alphabetically. For example, if I called your function with 'foo("snow",
# "glacier", "iceberg")</code> it should return <code>["GLACIER", "ICEBERG",
# "SNOW"]
def fix(*args):
    goal = []
    for things in args:
        print(things)
        y = things.upper()
        print(y)
        goal.append(y)
        goal.sort()
    print(goal)
    return goal


print(fix('snow', 'glacier', 'iceberg'))
