def tempcheck(value):
    if value > 25:
        return "Hot"
    elif value < 16:
        return "Cold"
    else:
        return "Warm"


foo1 = 26
foo2 = 25
foo3 = 16
foo4 = 15
print(tempcheck(foo1))
print(tempcheck(foo2))
print(tempcheck(foo3))
print(tempcheck(foo4))
