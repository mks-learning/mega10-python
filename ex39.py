# Define a function that takes as parameter a list that contains decimal
# numbers as strings and returns the sum of those numbers. For example,
# I called your function with <code>foo(['1.2', '2.6', '3.3'])</code> it
# should return <code>7.1</code>. Note that the floats of the input list
# are string datatypes.
def make_float(items):
    num_foo = []
    new_num = 0
    for item in items:
        if type(item) == str:
            num_foo.append(float(item))

    for item in num_foo:
        new_num += item
    return new_num


foo = ['1.2', '2.6', '3.3']
print(make_float(foo))
