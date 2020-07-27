def foo(value):
    retval = ''
    if value > 7:
        retval = "Warm"
    else:
        retval = "Cold"

    return retval


checktemp1 = 10
checktemp2 = 5

print(foo(checktemp1))
print(foo(checktemp2))
