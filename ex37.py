def is_it_a_num(items):
    num_foo = []
    for item in items:
        if type(item) != str:
            num_foo.append(item)
        else:
            num_foo.append(0)
    return num_foo


foo = [99, 'no data', 95, 94, 'no data']
# new_foo = [item if type(item) != str else 0 for item in items]
print(is_it_a_num(foo))
