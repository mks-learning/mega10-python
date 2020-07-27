def is_it_a_num(items):
    num_foo = []
    for item in items:
        if type(item) != str:
            num_foo.append(item)
    return num_foo


foo = [99, 'no data', 95, 94, 'no data']
print(is_it_a_num(foo))
