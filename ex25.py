
def foo(value):
    if len(value) > 8:
        answer = True
    else:
        answer = False

    return answer


val1 = 'mypass'
val2 = "mylongpassword"
print(foo(val1))
print(foo(val2))
